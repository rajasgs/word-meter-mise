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

app.config["PORT"]          = os.getenv("WMETER_BACKEND_PORT")

'''
    http://0.0.0.0:
'''
@app.route('/', methods = ['GET'])
def home_api():

    result_dict = {
        "city"       : "Toronto"
    }

    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(
        '0.0.0.0', 
        app.config["PORT"], 
        True
    )