__author__ = 'mili'
import json
import os
import flask
import smtplib, smtpd
from flask import Flask, session, request, render_template, flash, redirect, url_for, g, jsonify

app = Flask(__name__)


USERNAME = 'c8469ff849bfa3c7d7a749998c85b94c'
PASSWORD = 'f0546ae2b1486c2838cd3a7f36863246'
SENDER = 'chloe@parse-in1.mailjet.com'

from threading import Thread

@app.route("/email_process", methods = ['POST'])
def email_processor():
   data = request.data
   dataDict = json.loads(data)
   body = dataDict['Text-part']
   sender = dataDict['Sender']
   subject = dataDict['Subject']

   print(sender)
   print subject
   print(body)

   # Send e-mail back to sender
   send_mail(body, sender, find_commands(subject))

   return body

# PASS IN THE EMAIL
def find_commands(string):
    temp=[]

    for i in string.split("{{"):
        for j in i.split("}}"):
            temp.append(j)

    for n,i in enumerate(temp):
        if str(i).startswith("SEARCH"):
            # do the search here
            temp[n] = 'hello'
    return temp

def send_mail(text, receiver, subject):
   message = "\r\n".join([
        "From: %s" % SENDER,
        "To: %s" % receiver,
        "Subject: %s" % subject,
       text
        ])
   try:
      server = smtplib.SMTP('in-v3.mailjet.com:587')
      server.starttls()
      server.login(USERNAME,PASSWORD)
      server.sendmail(SENDER, receiver, message)
      server.quit()
      print "Successfully sent email to %s" % receiver
   except smtplib.SMTPException:
      print "Error: unable to send email to %s" % receiver

if __name__ =="__main__":
    app.run(debug =True)

#curl --user "c8469ff849bfa3c7d7a749998c85b94c:f0546ae2b1486c2838cd3a7f36863246" https://api.mailjet.com/v3/REST/parseroute -H "Content-Type: application/json" -d '{"Url":"https://700d664a.ngrok.com/email_process", "Email":"chloe@parse-in1.mailjet.com"}'