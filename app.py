from flask import Flask, render_template, redirect, request

import ImageCaption
import pyttsx3

# __name__ == __main__
app = Flask(__name__)
engine = pyttsx3.init()

@app.route('/')
def hello():
	return render_template("index2.html")
	speakcaption("welcome to the website")


@app.route('/', methods= ['POST'])
def marks():
	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/{}".format(f.filename)# ./static/images.jpg
		f.save(path)

		caption = ImageCaption.caption_this_image(path)
		
		result_dic = {
		'image' : path,
		'caption' : caption
		}
		speakcaption(caption)

	return render_template("index2.html", your_result =result_dic)

def speakcaption(caption):
	# Set properties for the text-to-speech engine (optional)
    # engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Speak the caption
    engine.say(caption)
    engine.runAndWait()
    



if __name__ == '__main__':
	# app.debug = True
	# due to versions of keras we need to pass another paramter threaded = Flase to this run function
	app.run(debug = True, threaded = False)
