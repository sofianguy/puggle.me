from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from measure import measure #from measure.py file, import measure() function
from bingSearch import search # from bingSearch import search
# from model import Bing, Website, BingWebsite, connect_to_db, db #from model.py import TableClasses, db

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def homepage():

	return render_template('homepage.html')

@app.route('/data-result')
def dataoutcome():
	user_input_url = request.args.get("url-input")
	website_url = "https://" + user_input_url
	data_measure = measure("https://" + user_input_url) #calling measure() function

	return render_template('data-result.html', website_url = website_url, 
		data_measure = data_measure)

@app.route('/bingSearchHomepage')
def bingsearch():

	return render_template('bingsearchhome.html')

@app.route('/bingSearchResult')
def bingResult():
	bing_input = request.args.get("bing_input")
	search_input = str(bing_input)
	search_list = search(search_input)

	page_data_structure_2 = []
	for s in search_list:
		page_data_structure_2.append({
		'title': s.title,
		'url': s.url,
		'description': s.description,
		'data': measure(s.url)
		})

	return render_template('bingresult.html', page_data_structure = page_data_structure_2)

if __name__ == '__main__':
	# debug=True gives us error messages in the browser and also "reloads" our web app
	# if we change the code.
	app.run(debug=True)
	
	# connect_to_db(app)

	# Use the DebugToolbar
	# DebugToolbarExtension(app)

