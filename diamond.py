from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import os

def main():
    app = ClarifaiApp()
    #image_set = create_image_set('/Users/mehty/Desktop/UofThacks/face-shape-recognition/Diamond/', ['diamond-face'])
    #app.inputs.bulk_create_images(image_set)
    model = app.models.create(model_id="face-shapes", concepts=['diamond-face'])
    model.train()
    #model = app.models.get('face-shapes')
    #url = raw_input("base64 encoded image bytes: ")
    #print model.predict_by_base64(url)['outputs'][0]['data']['concepts']

def create_image_set(img_path, concepts):
    images = []
    for file_path in glob(os.path.join(img_path, '*.jpg')):
    	print(file_path)
        img = ClImage(filename=file_path, concepts=concepts)
        images.append(img)

    return images

if __name__ == '__main__':
    main()