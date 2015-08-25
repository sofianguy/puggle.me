from py_bing_search import PyBingSearch

from sys import argv
from os import environ

import urllib
import requests

bing = PyBingSearch(environ['BING_API_KEY'])

def search3(search_string):
	
	result_list, next_uri = bing.search(search_string, limit=3, format='json') 
	#limit = how many search results

	return result_list

def search5(search_string):
	result_list, next_uri = bing.search(search_string, limit=5, format='json') 
	#limit = how many search results

	return result_list