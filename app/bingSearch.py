from py_bing_search import PyBingSearch

from sys import argv
from os import environ

import urllib
import requests

bing = PyBingSearch(environ['BING_API_KEY'])

def search(search_string, search_limit):
	result_list, next_uri = bing.search(search_string, limit=search_limit, format='json') 
	#limit = how many search results
	return result_list