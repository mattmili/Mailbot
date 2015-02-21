__author__ = 'mili'
import json
import os
import flask
from flask import Flask, session, request, render_template, flash, redirect, url_for, g, jsonify

app = Flask(__name__)

from threading import Thread

@app.route("/email_processor", methods = ['POST'])
def email_processor():
   data = request.data
   dataDict = json.loads(data)
   body = dataDict['Text-part']
   print(body)
   #send email back out

if __name__ =="__main__":
    app.run(debug =True)
