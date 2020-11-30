# coding=utf-8
from flask import Flask, request, send_file, render_template

from flask_qrcode import QRcode


app = Flask(__name__)
qrcode = QRcode(app)


@app.route('/')
def index():
    return "hello world lol"


@app.route('/qrcode', methods=['GET'])
def get_qrcode():
	# please get /qrcode?data=<qrcode_data>
	data = request.args.get('data', '')
	deviceid = request.args.get('deviceid', '')
	
	return render_template('template.html', data=data, deviceid=deviceid)

'''
if __name__ == '__main__':
    app.run(debug=False)
'''