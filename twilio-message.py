from twilio.rest import TwilioRestClient

from sys import argv
from os import environ

import urllib
import requests

account_sid = environ['TWILIO_ACCOUNT_SID']
auth_token  = environ['TWILIO_AUTH_TOKEN']

client = TwilioRestClient(account_sid, auth_token)