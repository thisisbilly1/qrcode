from flask import Flask, request
import pyqrcode
app = Flask(__name__)


@app.route('/')
def home():
	link = request.args.get('link')
	url = pyqrcode.create(link)
	return url

#app.run(debug=False)