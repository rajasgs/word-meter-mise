'''
Created on 
Course work: 
@author: Raja CSP
Source:
    
'''
# Import necessary modules

from flask import Flask, render_template, redirect, url_for, request, jsonify, session
import os
import requests

app = Flask(__name__)

SESSION_ID_KEY  = "sid"

app.config["PORT"]          = os.getenv("WMETER_MLMETER_PORT")
BACKEND_BASE                = os.getenv("BACKEND_BASE")

'''
    http://0.0.0.0:
'''
@app.route('/', methods = ['GET'])
def home_api():

    resp        = requests.get(BACKEND_BASE)
    resp_json   = resp.json()

    result_dict = {
        "one"       : "two",
        "result"    : resp_json,
        'backend_base' : BACKEND_BASE
    }

    return jsonify(result_dict)

if __name__ == '__main__':
    app.run('0.0.0.0', app.config["PORT"], True)