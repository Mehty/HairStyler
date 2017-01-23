from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import os



def round():
	image_set = create_image_set('/Users/mehty/Desktop/UofThacks/face-shape-recognition/round/', ['round-face'])
	app.inputs.bulk_create_images(image_set)

def square():
	image_set = create_image_set('Users/mehty/Desktop/UofThacks/face-shape-recognition/Square/', ['square-face'])
	app.inputs.bulk_create_images(image_set)

def heart():
	image_set = create_image_set('/Users/mehty/Desktop/UofThacks/face-shape-recognition/Heart/', ['heart-face'])
	app.inputs.bulk_create_images(image_set)

def diamond():
	image_set = create_image_set('/Users/mehty/Desktop/UofThacks/face-shape-recognition/Diamond/', ['diamond-face'])
	app.inputs.bulk_create_images(image_set)

def long_face():
	image_set = create_image_set('/Users/mehty/Desktop/UofThacks/face-shape-recognition/long/', ['long-face'])
	app.inputs.bulk_create_images(image_set)

def oval():
	image_set = create_image_set('/Users/mehty/Desktop/UofThacks/face-shape-recognition/oval/', ['oval-face'])
	app.inputs.bulk_create_images(image_set)

def train_round():
	model = app.models.create(model_id="face-shapes", concepts=['round-face'])
	model.train()

def train_square():
	model = app.models.create(model_id="face-shapes", concepts=['square-face'])
	model.train()

def train_heart():
	model = app.models.create(model_id="face-shapes", concepts=['heart-face'])
	model.train()

def train_diamond():
	model = app.models.create(model_id="face-shapes", concepts=['diamond-face'])
	model.train()

def train_long():
	model = app.models.create(model_id="face-shapes", concepts=['long-face'])
	model.train()

def train_oval():
	model = app.models.create(model_id="face-shapes", concepts=['oval-face'])
	model.train()


def main():
	app = ClarifaiApp()
	model = app.models.get('face-shapes')
	bytes = raw_input("base 64 encoded image bytes: ")
	print model.predict_by_base64(bytes)['outputs'][0]['data']['concepts']

def create_image_set(img_path, concepts):
    images = []
    for file_path in glob(os.path.join(img_path, '*.jpg')):
        print(file_path)
        img = ClImage(filename=file_path, concepts=concepts)
        images.append(img)

    print images

if __name__ == '__main__':
	main()

#if __name__ == '__round__':
#	round()

#if __name__ == '__square__':
#	square()

#if __name__ == '__h__':
#	heart()

#if __name__ == '__diamond__':
#	diamond()

#if __name__ == '__long_face__':
#	long_face()

#if __name__ == '__oval__':
#	oval()

if __name__ == '__train_square__':
	train_square()
