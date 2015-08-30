from flask import Flask, render_template, request, redirect
from measure import create_process, read_proc_results, measure 
# from measure.py file, import these functions
from bingSearch import search3, search5 # from bingSearch.py import search() functions
from twilio import twiml
from model import Result, connect_to_db, db #database stuff
from datetime import datetime
from sqlalchemy import update
import sqlite3
conn = sqlite3.connect('datauseresult.db') #connects to database called 'websizeresult'

app = Flask(__name__)

@app.route('/')
def bingSearch():

	return render_template('bingsearchhome.html')

@app.route('/result')
def bingResult():
	bing_input = request.args.get("bing_input")
	# bing_input is unicode
	search_input = str(bing_input)
	# if user doesn't type anything in search box
	if search_input == "":
		return redirect('/')

	search_list = search5(search_input)

	result_objects = []
	page_data_structure_2 = []
	for s in search_list:
		result = Result.query.filter_by(url=s.url).first()
		# if result is not True (meaning it has a query)
		if result:
			result_objects.append(result)
		else:
			page_data_structure_2.append({
			'title': s.title,
			'url': s.url,
			'description': s.description,
			})

	url_list = []
	for page_data in page_data_structure_2:
		url_list.append(page_data['url'])

	print "measuring", url_list
	measured_url_list = measure(url_list)

	for i in range(len(page_data_structure_2)):
		page_data_structure_2[i]['dsize'] = measured_url_list[i]

	# adds results to database
	for page_data in page_data_structure_2:
		bing_result_to_db = Result(url=page_data['url'], size=page_data['dsize'], 
			datetime=datetime.utcnow(), description=page_data['description'])
		db.session.add(bing_result_to_db)
		# **appends results to db**
		result_objects.append(bing_result_to_db)
	# then commits to database
	db.session.commit()

	return render_template('bingresult.html', results=result_objects)

@app.route('/twilioTest', methods=['POST'])
def twilioTest():
	text_body = request.values.get('Body')
	result_of_search_text_input = search3(text_body)
	print result_of_search_text_input

	result_objects = []
	twilio_foo = []
	for each in result_of_search_text_input:
		result = Result.query.filter_by(url=each.url).first()
		if result:
			result_objects.append(result)
		else:
			twilio_foo.append({
				'title': each.title,
				'url': each.url,
				'description': each.description
				})

	url_list = []
	for i in twilio_foo:
		url_list.append(i['url'])

	print "measuring", url_list
	measured_url_list = measure(url_list)

	for i in range(len(twilio_foo)):
		twilio_foo[i]['dsize'] = measured_url_list[i]

	for each in twilio_foo:
		bing_result_to_db = Result(url=each['url'], size=each['dsize'], 
			datetime=datetime.utcnow(), description=each['description'])
		db.session.add(bing_result_to_db)
		result_objects.append(bing_result_to_db)
	db.session.commit()

	result_message_to_user = ""
	for each in result_objects:
		result_message_to_user += each.url + " "
		result_message_to_user += each.size + "\n"
	
	# See message before sending SMS
	print result_message_to_user

	resp = twiml.Response()
	resp.message(result_message_to_user)

	return str(resp)


if __name__ == '__main__':
	# debug=True gives us error messages in the browser and also "reloads" our web app
	# if we change the code.
	connect_to_db(app)
	app.run(debug=True)

	# app.run()
