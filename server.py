from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension

from measure import measure #from measure.py file, import measure() function
from bingSearch import search # from bingSearch.py import search() function

from model import Result, connect_to_db, db #database stuff

from datetime import datetime

from sqlalchemy import update

import sqlite3
conn = sqlite3.connect('datauseresult.db') #connects to database called 'websizeresult'

app = Flask(__name__)

@app.route('/')
def bingsearch():

	return render_template('bingsearchhome.html')

@app.route('/result')
def bingResult():
	bing_input = request.args.get("bing_input")
	#bing_input is unicode
	search_input = str(bing_input)
	search_list = search(search_input)

	page_data_structure_2 = []
	for s in search_list:
		page_data_structure_2.append({
		'title': s.title,
		'url': s.url,
		'description': s.description,
		'dsize': measure(s.url)
		})

	#adds results to database
	for i in page_data_structure_2:
		bing_result_url_db = i['url']
		bing_result_data_db = i['dsize']
		bing_result_datetime_db = datetime.utcnow()

		bing_result_to_db = Result(url = bing_result_url_db, size = bing_result_data_db, 
			datetime = bing_result_datetime_db)
		db.session.add(bing_result_to_db)
		db.session.commit()

	return render_template('bingresult.html', page_data_structure = page_data_structure_2)


if __name__ == '__main__':
	# debug=True gives us error messages in the browser and also "reloads" our web app
	# if we change the code.

	connect_to_db(app)
	app.run(debug=True)

	# Use the DebugToolbar
	# DebugToolbarExtension(app)

	# app.run()
