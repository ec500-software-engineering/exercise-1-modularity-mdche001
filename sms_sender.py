#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright Mingdao Che mdche@bu.edu 2019#
# Reference: https://www.twilio.com/docs/sms/quickstart/python


from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import threading
import time
import random


# data type from the common_types
class Message(object):
    def __init__(self, content, urgency):
        self._content = content
        self._urgency = urgency

    def get_msg_content(self):
        return self._content

    def get_urgency(self):
        return self._urgency


# Your Account Sid and Auth Token from twilio.com/console
accountSID='authToken'
authToken='authToken'
myNumber='+1mynum'
twilioNumber='+1twilionum'
message= "Your blood pressure is 100/120"

# for general information #
class Contact(object):
    def __init__(self, name, sms_info, email_info):
        self._name = name
        self._sms_info = sms_info
        self._email_info = email_info

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email_info

    def get_sms(self):
        return self._sms_info



def textmyself(source_phone_num,destination_phone_num,message):
    """fuction to  send messages to the phone by twilio number"""
    # Getting the Authorization of the twilio
    delay = random.randrange(1, 100)
    time.sleep(delay)

    #send message by twilio api
    # twilioCli.api.account.messages.create(body=message,from_=twilioNumber,to=myNumber)//python2
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message,from_=twilioNumber,to=myNumber)#python3


def callmyself(source_phone_num, destination_phone_num,message):
    """ call the phone number by using an trial voice"""
    # Getting the Authorization of the twilio
    twilioCli = Client(accountSID, authToken)
    # call the phone number
    testcall = twilioCli.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml', # the trial voice's url
                            to='+18574728393',
                            from_='+18572148494'
                        )

    print(testcall.sid)


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Thanks so much for your reply, we will contact you as soon as possible!")

    return str(resp)

if __name__ == "__main__":
    # Msg = Message ('The patient is blooding', 0)
    # textmyself(myNumber,twilioNumber,message)
    # while(True):
    callmyself(myNumber,twilioNumber,message)
    # for i in range(5):
    #     _thread.start_new_thread(textmyself, (myNumber,twilioNumber,message))

    for i in range(5):
        t = threading.Thread(target=textmyself(myNumber,twilioNumber,message))
        t.start()
    # textmyself(Msg.get_msg_content()) # From the common types
    app.run(debug=True)