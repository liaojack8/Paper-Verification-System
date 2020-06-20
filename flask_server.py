#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import Response
from flask_cors import CORS
from flask_cors import cross_origin
import main
debug = False
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def getData():
	if request.method == 'POST':
		receviceData = request.get_data()
		if debug:print(receviceData.decode())
		data = json.loads(receviceData.decode())
		if ('timestamp' in data):
			return main.flask_func(data['title'], data['content'], data['timestamp'])
		else:
			return main.flask_func(data['title'], data['content'], time.time())
	else:
		return Response(
        'only support post request!',
        status=200
    	)

if __name__ =='__main__':
	app.run(host='0.0.0.0', debug=True, port=58088)