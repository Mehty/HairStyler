from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

def main():
	app = ClarifaiApp()
	model = app.models.get('general-v1.3')
	url = 'http://www.rd.com/wp-content/uploads/sites/2/2016/04/01-cat-wants-to-tell-you-laptop.jpg'
	image = ClImage(url)
	print image.base64
	#bytes = raw_input("base64: ")
	#print model.predict_by_base64(bytes)

if __name__ == '__main__':
	main()