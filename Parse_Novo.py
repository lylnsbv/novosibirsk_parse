import Config_Novo as Cnfg
from Data_Novo import Data as Dt

import os

# from random import uniform
from random import choice

from multiprocessing import Pool
from itertools import repeat

stop_loop = False


def main():

	end_num = ''

	'''  parse until -> set page number  '''
	while True:
		try:
			end_num = int(input('Сколько страниц парсит? Введите число: '))
			break
		except ValueError:
			print('\n', 'Введите только целое число!', '\n')
			continue

	'''   check file exists   '''
	if os.path.exists('Result/Csv_Data/Vtorichka_data.csv'):
		os.remove('Result/Csv_Data/Vtorichka_data.csv')
	if os.path.exists('Result/Csv_Data/Novostroiki_data.csv'):
		os.remove('Result/Csv_Data/Novostroiki_data.csv')
	if os.path.exists('Result/Csv_Data/Сommercial_data.csv'):
		os.remove('Result/Csv_Data/Сommercial_data.csv')
	if os.path.exists('Result/Csv_Data/Сommercial_land_data.csv'):
		os.remove('Result/Csv_Data/Сommercial_land_data.csv')
	if os.path.exists('Result/Csv_Data/Land_data.csv'):
		os.remove('Result/Csv_Data/Land_data.csv')

	'''   multiparse   '''
	# make_multi(Cnfg.url_list, Cnfg.url_n, end_num)
	pool = Pool(5)
	pool.starmap(make_multi, zip(Cnfg.url_list, Cnfg.url_n, repeat(end_num)))
	pool.close()
	pool.join()

	
def make_multi(url, url_n, end_num):
	#  ---  get proxy, header list  ---
	proxy = {"http:": "http://"f"{choice(Cnfg.proxy_list)}"}
	header = {"userAgent": f"{choice(Cnfg.user_agent_list)}"}

	print(proxy)
	print(header)

	global stop_loop

	for i in range(1, end_num + 1):

		print('\n' + 'Страница:', i)

		page_data = Dt(url.format(str(i)), url_n, header, proxy)

		html = page_data.get_products_html()

		stop_loop = page_data.stop_loop

		if stop_loop:
			print(f'Страница {str(i)} не существует!')
			break

		if html != "":
			page_data.get_products_data(html, i)

		stop_loop = page_data.stop_loop
		proxy = page_data.proxy
		header = page_data.header

		if stop_loop:
			print(f'Страница {str(i)} была последней')
			break

		# a=uniform(5, 10)
		# time.sleep(a)
	

if __name__ == '__main__':
	main()
