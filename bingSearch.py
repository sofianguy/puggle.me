from py_bing_search import PyBingSearch

import urllib
import requests

from sys import argv
from os import environ

bing = PyBingSearch(environ['BING_API_KEY'])


# def search(str):
# 	result_list, next_uri = bing.search(str, limit=4, format='json') 
# 	#limit = how many search results

# 	return result_list

# search('puppies')

result_list, next_uri = bing.search('puppies', limit=4, format='json') 

print result_list, next_uri