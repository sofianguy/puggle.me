from py_bing_search import PyBingSearch

import urllib
import requests

from sys import argv
from os import environ

bing = PyBingSearch(environ['BING_API_KEY'])


def search(search_string):
	
	result_list, next_uri = bing.search(search_string, limit=2, format='json') 
	#limit = how many search results

	return result_list


# search_list = search('puppy')
# output_search = ""
# for search in search_list:
# 	output_search = search.title, search.url
# 	print output_search
# self.title:         title of the result
# self.url:           the url of the result
# self.description:   description for the result
# self.id:            bing id for the page