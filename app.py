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
	#data = request.args.get('data', '')
	data ="https://apps.powerapps.com/play/2ef38032-cf7b-496f-90ca-4cb0d73c8edf?tenantId=a41c82de-1ce1-4077-8cee-685e4285be5c&source=portal"
	deviceid = request.args.get('deviceid', '')
	data+="&deviceid="+str(deviceid)
	
	return render_template('template.html', data=data, deviceid=deviceid)

'''
if __name__ == '__main__':
    app.run(debug=False)
'''