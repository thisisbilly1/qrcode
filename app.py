from flask import Flask
import requests
import pyqrcode
app = Flask(__name__)


@app.route('/')
def home():
	link = requests.args.get('link')
	url = pyqrcode.create(link)
	return url

#app.run(debug=False)