from py_bing_search import PyBingSearch

import urllib
import requests

from sys import argv
from os import environ

bing = PyBingSearch(environ['BING_API_KEY'])


def search(str):
	
	result_list, next_uri = bing.search(str, limit=4, format='json') 
	#limit = how many search results

	return result_list


search_list = search('puppies') #returns a list of objects

for search in search_list:
	print search.title, search.url
	
# self.title:         title of the result
# self.url:           the url of the result
# self.description:   description for the result
# self.id:            bing id for the page
