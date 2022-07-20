import requests
from bs4 import BeautifulSoup


class Proxies:

	def get_proxy_online_proxy(self):

		proxy_list = []
		url = 'http://online-proxy.ru/index.html?city=%CD%EE%E2%EE%F1%E8%E1%E8%F0%F1%EA'

		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')

		table = soup.find('table').find('td', class_='content').find('table', attrs={"border": "0"}).select(
			'tr td:nth-of-type(2), td:nth-of-type(3), td:nth-of-type(5)'
		)[1:]
		td = [tr.get_text() for tr in table[2:]]

		for item1, item2, item3 in zip(td[::3], td[1::3], td[2::3]):

			if item3 == 'ýëèòíûé':
				proxy_list.append(item1 + ':' + item2)

		return proxy_list

	def get_proxy_scrapingant(self):

		proxy_list = []
		url = 'https://scrapingant.com/free-proxies/'

		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')

		tr_list = soup.find('table', class_='proxies-table').find_all('tr')[1:]
		proxy_list = [x.find('td').get_text() for x in tr_list]

		return proxy_list

	def get_proxy_proxypedia(self):

		proxy_list = []
		url = 'https://proxypedia.org/'

		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')

		table = soup.find('main').find('ul').find_all('li')	
		proxy_list = [x.find('a').get_text() for x in table[1:]]

		return proxy_list

	def get_proxy_htmlweb(self):

		proxy_list = []
		url = 'https://htmlweb.ru/analiz/proxy_list.php?type%5B%5D=1&country%5B%5D=RU&perpage=20'

		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')

		table = soup.find('table', class_='tbl').find_all('tr')
		proxy_list = [x.find('td').get_text() for x in table[1:]][::2]
		
		return proxy_list
