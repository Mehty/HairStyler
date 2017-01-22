from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import os

def main():
	app = ClarifaiApp()
	model = app.models.get('general-v1.3')
	
	bytes = raw_input("base64: ")
	print model.predict_by_base64(bytes)['outputs'][0]['data']['concepts']

def create_image_set(img_path):
	app = ClarifaiApp()
	model = app.models.get('general-v1.3')
	images = {}
	for file_path in glob(os.path.join(img_path, '*.jpg')):
		print(file_path)
		images[file_path] = model.predict_by_filename(file_path)['outputs'][0]['data']['concepts']

	return images

hairstyles = create_image_set('/Users/mehty/Desktop/hairstyle/')

print hairstyles