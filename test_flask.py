#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:51:04 2019

@author: nicolas
"""

from flask import Flask, jsonify

from iris_postgresql import IrisPostgres

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = {'id':123,'name':'Flask test'}
    return jsonify(message)

@app.route('/postgres')
def postgres():
    iris_postgres = IrisPostgres()
    dataframe = iris_postgres.getDataframe()
    data_json = dataframe.to_json(orient='records')
    return jsonify(data_json)

if __name__ == '__main__':
    app.debug = True #Nos muestra los errores en el proceso
    app.run()