from py_bing_search import PyBingSearch

from sys import argv
from os import environ

import urllib
import requests

bing = PyBingSearch(environ['BING_API_KEY'])

def search(search_string):
	
	result_list, next_uri = bing.search(search_string, limit=2, format='json') 
	#limit = how many search results

	return result_list