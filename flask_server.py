#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import main
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getData():
    if request.method == 'POST':
        a = request.get_data()
        data = json.loads(a.decode())['data']
        print(data)
        return main.flask_func(data['title'], data['content'], data['timestamp'])
    else:
        return '<h1>only support post request!</h1>'

if __name__ =='__main__':
    app.run(debug=True,port=58088)