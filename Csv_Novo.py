import os
import csv


class Csv:

	dir_path = os.getcwd()
	
	def write_vtorichka(self, data):

		img_path = r'=ГИПЕРССЫЛКА("{}\Result\Vtorichka\{}")'.format(self.dir_path, data['Id'])
		
		with open('Result/Csv_Data/Vtorichka_data.csv', 'a') as fd:

			if fd.tell() == 0:			
				writer = csv.DictWriter(fd, data, delimiter=';', lineterminator='\n')
				writer.writeheader()

			writer = csv.writer(fd, delimiter=';', lineterminator='\n')
			writer.writerow((
							data['Id'],
							data['Ссылка на объект (URL)'],
							data['Дата добавления'],
							data['Статус'],
							data['Цена'],
							data['Цена квадратного метр'],
							data['Город'],
							data['Район'],
							data['Микрорайон'],
							data['Улица'],
							data['Номер дома'],
							data['широта'],
							data['долгота'],
							data['Количество комнат'],
							data['Общая площадь'],
							data['Этаж'],
							data['Этажность'],
							data['Тип квартиры'],
							data['Тип дома'],
							data['Год постройки'],
							data['Ближайшая станция метро'],
							data['Расстояние до метро'],
							data['Пешком/Транспортом'],
							img_path
			))

	def write_novostroiki(self, data):
	
		img_path = r'=ГИПЕРССЫЛКА("{}\Result\Novostroiki\{}")'.format(self.dir_path, data['Id'])
		
		with open('Result/Csv_Data/Novostroiki_data.csv', 'a') as fd:

			if fd.tell() == 0:			
				writer = csv.DictWriter(fd, data, delimiter=';', lineterminator='\n')
				writer.writeheader()

			writer = csv.writer(fd, delimiter=';', lineterminator='\n')
			writer.writerow((
							data['Id'],
							data['Ссылка на объект (URL)'],
							data['Дата добавления'],
							data['Статус'],
							data['Цена'],
							data['Цена квадратного метр'],
							data['Город'],
							data['Район'],
							data['Микрорайон'],
							data['Улица'],
							data['Номер дома'],
							data['широта'],
							data['долгота'],
							data['Количество комнат'],
							data['Общая площадь'],
							data['Этаж'],
							data['Этажность'],
							data['Тип квартиры'],
							data['Тип дома'],
							data['Год постройки'],
							data['Наименование жилого комплекса'],
							data['Застройщик жилого комплекса'],
							data['Срок завершения строительства'],
							data['Ближайшая станция метро'],
							data['Расстояние до метро'],
							data['Пешком/Транспортом'],
							img_path
			))
	
	def write_commercial(self, data):
		
		img_path = r'=ГИПЕРССЫЛКА("{}\Result\Сommercial\{}")'.format(self.dir_path, data['Id'])

		with open('Result/Csv_Data/Сommercial_data.csv', 'a') as fd:

			if fd.tell() == 0:			
				writer = csv.DictWriter(fd, data, delimiter=';', lineterminator='\n')
				writer.writeheader()

			writer = csv.writer(fd, delimiter=';', lineterminator='\n')
			writer.writerow((
							data['Id'],
							data['Ссылка на объект (URL)'],
							data['Дата добавления'],
							data['Статус'],
							data['Цена'],
							data['Цена квадратного метр'],
							data['Город'],
							data['Район'],
							data['Микрорайон'],
							data['Улица'],
							data['Номер дома'],
							data['широта'],
							data['долгота'],
							data['Категория недвижимость'],
							data['Описание'],
							data['Контакты'],
							img_path
			))

	def write_commercial_land(self, data):
		
		img_path = r'=ГИПЕРССЫЛКА("{}\Result\Сommercial_land\{}")'.format(self.dir_path, data['Id'])
		
		with open('Result/Csv_Data/Сommercial_land_data.csv', 'a') as fd:

			if fd.tell() == 0:			
				writer = csv.DictWriter(fd, data, delimiter=';', lineterminator='\n')
				writer.writeheader()

			writer = csv.writer(fd, delimiter=';', lineterminator='\n')
			writer.writerow((
							data['Id'],
							data['Ссылка на объект (URL)'],
							data['Дата добавления'],
							data['Статус'],
							data['Цена'],
							data['Цена за сотку'],
							data['Город'],
							data['Район'],
							data['Микрорайон'],
							data['Улица'],
							data['Номер дома'],
							data['широта'],
							data['долгота'],
							data['Площадь участка'],
							data['Категория земельного участка'],
							data['Описание'],
							data['Контакты'],
							img_path
			))

	def write_land(self, data):

		img_path = r'=ГИПЕРССЫЛКА("{}\Result\Land\{}")'.format(self.dir_path, data['Id'])
		
		with open('Result/Csv_Data/Land_data.csv', 'a') as fd:
			
			if fd.tell() == 0:		
				writer = csv.DictWriter(fd, data, delimiter=';', lineterminator='\n')
				writer.writeheader()		

			writer = csv.writer(fd, delimiter=';', lineterminator='\n')
			writer.writerow((
							data['Id'],
							data['Ссылка на объект (URL)'],
							data['Дата добавления'],
							data['Статус'],
							data['Цена'],
							data['Цена за сотку'],
							data['Город'],
							data['Район'],
							data['Микрорайон'],
							data['Улица'],
							data['Номер дома'],
							data['широта'],
							data['долгота'],
							data['Площадь участка'],
							data['Категория земельного участка'],
							data['Описание'],
							data['Контакты'],
							img_path
			))
