import os
import requests


class Image:

	def write_vtorichka_image(self, data_id, photos):

		path = f'Result/Vtorichka/{data_id}/'

		if not os.path.exists(path):
			os.makedirs(path)

		for photo in photos:
			try:
				response_photo = requests.get(photo['fullUrl'], stream=True)
				filename = path + str(photo['id']) + '.jpg'

				if response_photo.ok:

					with open(filename, 'wb') as photo_handle:
												
						for block in response_photo.iter_content(1024):
							if not block:
								break
							photo_handle.write(block)

					photo_handle.close()
			except:
				print('Сохранить файлы не удалось.')

	def write_novostroiki_image(self, data_id, photos):

		path = f'Result/Novostroiki/{data_id}/'

		if not os.path.exists(path):
			os.makedirs(path)

		for photo in photos:
			try:
				response_photo = requests.get(photo['fullUrl'], stream=True)
				filename = path + str(photo['id']) + '.jpg'

				if response_photo.ok:

					with open(filename, 'wb') as photo_handle:
												
						for block in response_photo.iter_content(1024):
							if not block:
								break
							photo_handle.write(block)

					photo_handle.close()
			except:
				print('Сохранить файлы не удалось.')

	def write_commercial_image(self, data_id, photos):

		path = f'Result/Commercial/{data_id}/'

		if not os.path.exists(path):
			os.makedirs(path)

		for photo in photos:
			try:
				response_photo = requests.get(photo['fullUrl'], stream=True)
				filename = path + str(photo['id']) + '.jpg'

				if response_photo.ok:

					with open(filename, 'wb') as photo_handle:
												
						for block in response_photo.iter_content(1024):
							if not block:
								break
							photo_handle.write(block)

					photo_handle.close()
			except:
				print('Сохранить файлы не удалось.')

	def write_commercial_land_image(self, data_id, photos):

		path = f'Result/Commercial_Land/{data_id}/'

		if not os.path.exists(path):
			os.makedirs(path)

		for photo in photos:
			try:
				response_photo = requests.get(photo['fullUrl'], stream=True)
				filename = path + str(photo['id']) + '.jpg'

				if response_photo.ok:

					with open(filename, 'wb') as photo_handle:
												
						for block in response_photo.iter_content(1024):
							if not block:
								break
							photo_handle.write(block)

					photo_handle.close()
			except:
				print('Сохранить файлы не удалось.')

	def write_land_image(self, data_id, photos):

		path = f'Result/Land/{data_id}/'

		if not os.path.exists(path):
			os.makedirs(path)

		for photo in photos:
			try:
				response_photo = requests.get(photo['fullUrl'], stream=True)

				filename = path + str(photo['id']) + '.jpg'

				if response_photo.ok:

					with open(filename, 'wb') as photo_handle:
												
						for block in response_photo.iter_content(1024):
							if not block:
								break
							photo_handle.write(block)

					photo_handle.close()
			except:
				print('Сохранить файлы не удалось.')
