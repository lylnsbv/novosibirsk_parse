import requests
from random import choice
import time
from datetime import datetime
from bs4 import BeautifulSoup
import json
import Config_Novo as Config
from Csv_Novo import Csv
from Image_Novo import Image


class Data:

	stop_loop = False
	captcha_title = 'Captcha - база объявлений ЦИАН'

	def __init__(self, url, csv_n, header, proxy):
		self.url = url
		self.header = header
		self.proxy = proxy
		self.csv_n = csv_n
	
	def get_products_html(self):

		html = ""

		try:
			while True:

				response = requests.get(self.url, headers=self.header, proxies=self.proxy)

				if self.captcha_title not in response.text:
					break
				else:
					print(self.captcha_title)					
					print('\n' + 'IP в блокировке, ждите! Проверка следующего парсинга начнется через час' + '\n')
					time.sleep(900)
					self.proxy = {"http:": "http://" + choice(Config.proxy_list)}
					self.header = {"userAgent": f"{choice(Config.user_agent_list)}"}
					print(self.proxy)
					print(self.header)

			if response.ok:

				if self.csv_n == 1:
					with open('page_data/vtorichka_products_parse.html', 'w', encoding='utf-8') as f:
						f.write(response.text)

					with open('page_data/vtorichka_products_parse.html', 'r', encoding='utf-8') as f:
						html = f.read()
						f.close()
				if self.csv_n == 2:
					with open('page_data/novostroik_products_parse.html', 'w', encoding='utf-8') as f:
						f.write(response.text)

					with open('page_data/novostroik_products_parse.html', 'r', encoding='utf-8') as f:
						html = f.read()
						f.close()
				if self.csv_n == 3:
					with open('page_data/commercial_products_parse.html', 'w', encoding='utf-8') as f:
						f.write(response.text)
					with open('page_data/commercial_products_parse.html', 'r', encoding='utf-8') as f:
						html = f.read()
						f.close()
				if self.csv_n == 4:
					with open('page_data/commercial_land_products_parse.html', 'w', encoding='utf-8') as f:
						f.write(response.text)
					with open('page_data/commercial_land_products_parse.html', 'r', encoding='utf-8') as f:
						html = f.read()
						f.close()
				if self.csv_n == 5:
					with open('page_data/land_products_parse.html', 'w', encoding='utf-8') as f:
						f.write(response.text)
					with open('page_data/land_products_parse.html', 'r', encoding='utf-8') as f:
						html = f.read()
						f.close()
			else:		
				print(response.status_code)		
				self.stop_loop = True

		except():
			pass

		return html

	def get_products_data(self, html, i_num):

		start_products_json = '"offers":['

		if start_products_json in html:
			start = html.index(start_products_json) + len(start_products_json)-1

			if self.csv_n == 1 or self.csv_n == 2 or self.csv_n == 5:
				end = html.index(',"paginationUrls":', start)
			else:
				end = html.index(',"aggregatedOffers":', start)

			json_raw = html[start:end].strip()

			#  ---   Checking if json format is correct   ---
			# with open('ck.json', 'w', encoding='utf-8') as f:
			# json.dump(json_raw, f, ensure_ascii=False, indent=4)

			json_data = json.loads(json_raw)

			if self.csv_n == 1:
				object_type = 'flat'
				self.get_vtorichka_card_data(json_data, object_type)
			elif self.csv_n == 2:
				object_type = 'flat'
				self.get_novostroik_card_data(json_data, object_type)
			elif self.csv_n == 3:
				object_type = 'commercial'
				self.get_commercial_card_data(json_data, object_type)
			elif self.csv_n == 4:
				object_type = 'commercial'
				self.get_commercial_land_card_data(json_data, object_type)
			elif self.csv_n == 5:
				object_type = 'suburban'
				self.get_land_card_data(json_data, object_type)

		soup = BeautifulSoup(html, 'lxml')
		page_number = soup.find("div", {"data-name": "Pagination"}).select('li')[-1].get_text()
		print(page_number)
			
		if page_number.isdigit() and i_num == int(page_number):
			self.stop_loop = True

	def get_vtorichka_card_data(self, data, object_type):

		for item in data:
			city = ''
			okru = ''
			raion = ''
			mikro = ''
			street = ''
			house = ''

			metro_name = []
			metro_time = []
			metro_travel_type = []
			ad_id = item['cianId']
			public_stand_time = ''.join(item['creationDate'].split('.')[0])
			public_date = datetime.strptime(public_stand_time, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")

			status = item['status']

			if status == 'published':
				status = 'опубликован'

			price = item['bargainTerms']['price']
			address = item['geo']['address']

			for adr_item in address:
				if adr_item['locationTypeId'] == 1 and adr_item['type'] == 'location':
					city = adr_item['name']
				# elif adr_item['type'] == 'okrug':
				# okru = adr_item['name']
				elif adr_item['type'] == 'raion':
					raion = adr_item['name']
				elif adr_item['type'] == 'mikroraion':
					mikro = adr_item['name']
				elif adr_item['type'] == 'street':
					street = adr_item['name']
				elif adr_item['type'] == 'house':
					house = adr_item['name'] + '\t'

			lat = item['geo']['coordinates']['lat']
			lng = item['geo']['coordinates']['lng']
			rooms_count = item['roomsCount']
			total_area = item['totalArea'] + '\t'
			price_sqm = round(float(price) / float(total_area))

			floor_number = item['floorNumber']
			floors_count = item['building']['floorsCount']

			flat_key = item['flatType']
			flat_type = {
				'rooms': 'Номера',
				'studio': 'Студия',
				'openPlan': 'Квартира свободной планировки'
			}.get(flat_key, item['flatType'])

			house_material_key = item['building']['materialType']
			house_material_type = {
				'none': '',
				'brick': 'Кирпичный',
				'panel': 'Панельный',
				'monolith': 'Монолитный',
				'monolithBrick': 'Монолитно-кирпичный',
				'block': 'Блочный',
				'wood': 'Деревянный'
			}.get(house_material_key, item['building']['materialType'])

			year_release = item['building']['buildYear']

			undergrounds = item['geo']['undergrounds']

			for met_item in undergrounds:

				metro_name.append(met_item['name'])

				met_time = met_item['time']
				if met_time is not None and met_time != 'null':
					metro_time.append(met_time)

				if met_item['transportType'] == 'walk':
					travel_type = 'пешком'
				elif met_item['transportType'] == 'transport':
					travel_type = 'на транспорте'
				else:
					travel_type = met_item['travelType']

				metro_travel_type.append(travel_type)

			photos = [photo for photo in item['photos']]

			data_csv = {
						'Id': ad_id,
						'Ссылка на объект (URL)': f'=ГИПЕРССЫЛКА("{Config.card_url.format(object_type, ad_id)}")',
						'Дата добавления': public_date,
						'Статус': status,
						'Цена': price,
						'Цена квадратного метр': price_sqm,
						'Город': city,
						'Район': raion,
						'Микрорайон': mikro,
						'Улица': street,
						'Номер дома': house,
						'широта': lat,
						'долгота': lng,
						'Количество комнат': rooms_count,
						'Общая площадь': total_area,
						'Этаж': floor_number,
						'Этажность': floors_count,
						'Тип квартиры': flat_type,
						'Тип дома': house_material_type,
						'Год постройки': year_release,
						'Ближайшая станция метро': str(metro_name)[1:-1],
						'Расстояние до метро': str(metro_time)[1:-1],
						'Пешком/Транспортом': str(metro_travel_type)[1:-1],
						'Фото_адрес': photos}

			Csv().write_vtorichka(data_csv)
			Image().write_vtorichka_image(data_csv['Id'], data_csv['Фото_адрес'])

	def get_novostroik_card_data(self, data, object_type):

		for item in data:
			city = ''
			okru = ''
			raion = ''
			mikro = ''
			street = ''
			house = ''

			metro_name = []
			metro_time = []
			metro_travel_type = []

			ad_id = item['cianId']

			public_stand_time = ''.join(item['creationDate'].split('.')[0])
			public_date = datetime.strptime(public_stand_time, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")

			status = item['status']

			if status == 'published':
				status = 'опубликован'

			price = item['bargainTerms']['price']
			address = item['geo']['address']

			for adr_item in address:
				if adr_item['locationTypeId'] == 1 and adr_item['type'] == 'location':
					city = adr_item['name']
				# elif adr_item['type'] == 'okrug':
				# okru = adr_item['name']
				elif adr_item['type'] == 'raion':
					raion = adr_item['name']
				elif adr_item['type'] == 'mikroraion':
					mikro = adr_item['name']
				elif adr_item['type'] == 'street':
					street = adr_item['name']
				elif adr_item['type'] == 'house':
					house = adr_item['name'] + '\t'

			lat = item['geo']['coordinates']['lat']
			lng = item['geo']['coordinates']['lng']
			rooms_count = item['roomsCount']
			total_area = str(item['totalArea']) + '\t' if item['totalArea'] is not None else 1
			price_sqm = round(float(price) / float(total_area))

			floor_number = item['floorNumber']
			floors_count = item['building']['floorsCount']

			flat_key = item['flatType']
			flat_type = {
				'rooms': 'Номера',
				'studio': 'Студия',
				'openPlan': 'Квартира свободной планировки'
			}.get(flat_key, item['flatType'])

			house_material_key = item['building']['materialType']
			house_material_type = {
				'none': '',
				'brick': 'Кирпичный',
				'panel': 'Панельный',
				'monolith': 'Монолитный',
				'monolithBrick': 'Монолитно-кирпичный',
				'block': 'Блочный',
				'wood': 'Деревянный'
			}.get(house_material_key, item['building']['materialType'])

			year_release = item['building']['buildYear']

			new_building_name = item['newbuilding']['name']
			company_name = item['user']['companyName'] if item['user'] is not None and 'companyName' in item['user'] else ''
			quarter_end = item['building']['deadline']['quarterEnd'] \
				if item['building']['deadline'] is not None \
				and item['building']['deadline']['quarterEnd'] is not None else ''

			undergrounds = item['geo']['undergrounds']

			for met_item in undergrounds:

				metro_name.append(met_item['name'])

				met_time = met_item['time']
				if met_time is not None and met_time != 'null':
					metro_time.append(met_time)

				if met_item['transportType'] == 'walk':
					travel_type = 'пешком'
				elif met_item['transportType'] == 'transport':
					travel_type = 'на транспорте'
				else:
					travel_type = met_item['travelType']

				metro_travel_type.append(travel_type)

			photos = [photo for photo in item['photos']]

			data_csv = {
				'Id': ad_id,
				'Ссылка на объект (URL)': f'=ГИПЕРССЫЛКА("{Config.card_url.format(object_type, ad_id)}")',
				'Дата добавления': public_date,
				'Статус': status,
				'Цена': price,
				'Цена квадратного метр': price_sqm,
				'Город': city,
				'Район': raion,
				'Микрорайон': mikro,
				'Улица': street,
				'Номер дома': house,
				'широта': lat,
				'долгота': lng,
				'Количество комнат': rooms_count,
				'Общая площадь': total_area,
				'Этаж': floor_number,
				'Этажность': floors_count,
				'Тип квартиры': flat_type,
				'Тип дома': house_material_type,
				'Год постройки': year_release,
				'Наименование жилого комплекса': new_building_name,
				'Застройщик жилого комплекса': company_name,
				'Срок завершения строительства': quarter_end,
				'Ближайшая станция метро': str(metro_name)[1:-1],
				'Расстояние до метро': str(metro_time)[1:-1],
				'Пешком/Транспортом': str(metro_travel_type)[1:-1],
				'Фото_адрес': photos}
			
			Csv().write_novostroiki(data_csv)
			Image().write_novostroiki_image(data_csv['Id'], data_csv['Фото_адрес'])
		
	def get_commercial_card_data(self, data, object_type):

		for item in data:
			city = ''
			okru = ''
			raion = ''
			mikro = ''
			street = ''
			house = ''

			ad_id = item['cianId']

			public_stand_time = ''.join(item['creationDate'].split('.')[0])
			public_date = datetime.strptime(public_stand_time, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")

			status = item['status']

			if status == 'published':
				status = 'опубликован'

			price = item['bargainTerms']['price']
			address = item['geo']['address']

			for adr_item in address:
				if adr_item['locationTypeId'] == 1 and adr_item['type'] == 'location':
					city = adr_item['name']
				# elif adr_item['type'] == 'okrug':
				# okru = adr_item['name']
				elif adr_item['type'] == 'raion':
					raion = adr_item['name']
				elif adr_item['type'] == 'mikroraion':
					mikro = adr_item['name']
				elif adr_item['type'] == 'street':
					street = adr_item['name']
				elif adr_item['type'] == 'house':
					house = adr_item['name'] + '\t'

			lat = item['geo']['coordinates']['lat']
			lng = item['geo']['coordinates']['lng']
			total_area = item['totalArea'] + '\t'
			price_sqm = round(float(price) / float(total_area))

			category_key = item['category']
			category = {
				'officeSale': 'Офис',
				'freeAppointmentObjectSale': 'Помещение свободного назначения',
				'businessSale': 'Готовый бизнес',
				'warehouseSale': 'Склад',
				'shoppingAreaSale': 'Торговая площадь',
				'buildingSale': 'Здание',
				'industrySale': 'Производство'
			}.get(category_key, item['category'])

			description = item['description']

			phones = ', '.join('+' + elm['countryCode'] + elm['number'] for elm in item['phones'])

			photos = [photo for photo in item['photos']]

			data_csv = {
						'Id': ad_id,
						'Ссылка на объект (URL)': f'=ГИПЕРССЫЛКА("{Config.card_url.format(object_type, ad_id)}")',
						'Дата добавления': public_date,
						'Статус': status,
						'Цена': price,
						'Цена квадратного метр': price_sqm,
						'Город': city,
						'Район': raion,
						'Микрорайон': mikro,
						'Улица': street,
						'Номер дома': house,
						'широта': lat,
						'долгота': lng,
						'Категория недвижимость': category,
						'Описание': description.replace("\xb2", "2"),
						'Контакты': phones,
						'Фото_адрес': photos}

			Csv().write_commercial(data_csv)
			Image().write_commercial_image(data_csv['Id'], data_csv['Фото_адрес'])

	def get_commercial_land_card_data(self, data, object_type):

		for item in data:

			city = ''
			# okru = ''
			raion = ''
			mikro = ''
			street = ''
			house = ''

			ad_id = item['cianId']

			public_stand_time = ''.join(item['creationDate'].split('.')[0])
			public_date = datetime.strptime(public_stand_time, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")

			status = item['status']

			if status == 'published':
				status = 'опубликован'

			price = item['bargainTerms']['priceRur']
			address = item['geo']['address']

			for adr_item in address:
				if adr_item['locationTypeId'] == 1 and adr_item['type'] == 'location':
					city = adr_item['name']
				# elif adr_item['type'] == 'okrug':
				# okru = adr_item['name']
				elif adr_item['type'] == 'raion':
					raion = adr_item['name']
				elif adr_item['type'] == 'mikroraion':
					mikro = adr_item['name']
				elif adr_item['type'] == 'street':
					street = adr_item['name']
				elif adr_item['type'] == 'house':
					house = adr_item['name'] + '\t'

			lat = item['geo']['coordinates']['lat']
			lng = item['geo']['coordinates']['lng']

			area = item['land']['area'] + '\t'
			price_sqm = round(float(price) / float(area))

			category_key = item['land']['status']
			category = {
				'settlements': 'Участок поселений',
				'industryTransportCommunications': 'Земли промышленности',
				'forAgriculturalPurposes': 'Участок сельскохозяйственного назначения'
			}.get(category_key, item['land']['status'])

			description = item['description']

			phones = ', '.join('+' + elm['countryCode'] + elm['number'] for elm in item['phones'])

			photos = [photo for photo in item['photos']]

			data_csv = {
						'Id': ad_id,
						'Ссылка на объект (URL)': f'=ГИПЕРССЫЛКА("{Config.card_url.format(object_type, ad_id)}")',
						'Дата добавления': public_date,
						'Статус': status,
						'Цена': price,
						'Цена за сотку': price_sqm,
						'Город': city,
						'Район': raion,
						'Микрорайон': mikro,
						'Улица': street,
						'Номер дома': house,
						'широта': lat,
						'долгота': lng,
						'Площадь участка': area,
						'Категория земельного участка': category,
						'Описание': description.replace("\xb2", "2"),
						'Контакты': phones,
						'Фото_адрес': photos}
			
			Csv().write_commercial_land(data_csv)
			Image().write_commercial_land_image(data_csv['Id'], data_csv['Фото_адрес'])

	def get_land_card_data(self, data, object_type):

		for item in data:

			city = ''
			# okru = ''
			raion = ''
			mikro = ''
			street = ''
			house = ''

			ad_id = item['cianId']

			public_stand_time = ''.join(item['creationDate'].split('.')[0])
			public_date = datetime.strptime(public_stand_time, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")

			status = item['status']

			if status == 'published':
				status = 'опубликован'

			price = item['bargainTerms']['priceRur']
			address = item['geo']['address']

			for adr_item in address:
				if (adr_item['locationTypeId'] == 1 or adr_item['locationTypeId'] == 2) and adr_item['type'] == 'location':
					city = adr_item['name']
				# elif adr_item['type'] == 'okrug':
				# okru = adr_item['name']
				elif adr_item['type'] == 'raion':
					raion = adr_item['name']
				elif adr_item['type'] == 'mikroraion':
					mikro = adr_item['name']
				elif adr_item['type'] == 'street':
					street = adr_item['name']
				elif adr_item['type'] == 'house':
					house = adr_item['name'] + '\t'

			lat = item['geo']['coordinates']['lat']
			lng = item['geo']['coordinates']['lng']

			area = item['land']['area'] + '\t'
			price_sqm = round(float(price) / float(area))

			category_key = item['land']['status']
			category = {
				'suburbanNonProfitPartnership': 'Дачное некоммерческое партнерство',
				'individualHousingConstruction': 'Индивидуальное жилищное строительство',
				'privateFarm': 'Личное подсобное хозяйство',
				'industrialLand': 'Земля промышленного назначения',
				'gardening': 'Садоводство',
				'settlements': 'Участок поселений'
			}.get(category_key, item['land']['status'])

			description = item['description']

			phones = ', '.join('+' + elm['countryCode'] + elm['number'] for elm in item['phones'])

			photos = [photo for photo in item['photos']]

			data_csv = {
						'Id': ad_id,
						'Ссылка на объект (URL)': f'=ГИПЕРССЫЛКА("{Config.card_url.format(object_type, ad_id)}")',
						'Дата добавления': public_date,
						'Статус': status,
						'Цена': price,
						'Цена за сотку': price_sqm,
						'Город': city,
						'Район': raion,
						'Микрорайон': mikro,
						'Улица': street,
						'Номер дома': house,
						'широта': lat,
						'долгота': lng,
						'Площадь участка': area,
						'Категория земельного участка': category,
						'Описание': description.replace("\xb2", "2"),
						'Контакты': phones,
						'Фото_адрес': photos}

			Csv().write_land(data_csv)
			Image().write_land_image(data_csv['Id'], data_csv['Фото_адрес'])
