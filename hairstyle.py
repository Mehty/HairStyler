from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import os

def prediction(bytes):
	app = ClarifaiApp()
	model = app.models.get('general-v1.3')
	
	return model.predict_by_base64(bytes)['outputs'][0]['data']['concepts']

def create_image_set(img_path):
	app = ClarifaiApp()
	model = app.models.get('general-v1.3')
	images = {}
	for file_path in glob(os.path.join(img_path, '*.jpg')):
		#print(file_path)
		images[file_path] = model.predict_by_filename(file_path)['outputs'][0]['data']['concepts']

	return images


#print hairstyles

def main():
	byte = raw_input("base64: ")
	hairstyles = create_image_set('/Users/mehty/Desktop/hairstyle/')
	pic = prediction(byte)
	c1 = 0
	c2 = 0
	tags = {}
	lst = []
	for k, v in hairstyles.items():
		for i in v:
			for x in pic:
				if x['name'] == i['name']:
					c1 += 1
					tags[i['name']] = i['value']
					c2 += i['value']
		if  len(lst) == 0:
			lst.append([tags, c1, c2, k])
			c1 = 0
			c2 = 0
			tags = {}
		elif c1 > lst[0][1]:
			del lst[:]
			lst.append([tags, c1, c2, k])
			c1 = 0
			c2 = 0
			tags = {}
		elif c1 == lst[0][1]:
			if c2 > lst[0][2]:
				del lst[:]
				lst.append([tags, c1, c2, k])
				c1 = 0
				c2 = 0
				tags = {}
			elif c2 == lst[0][2]:
				lst.append([tags, c1, c2, k])
				c1 = 0
				c2 = 0
				tags = {}
	print lst

if __name__ == '__main__':
	main()








