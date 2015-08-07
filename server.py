from flask import Flask, render_template, request

from measure import measure #from measure.py file, import measure() function

# from bingSearch import search # from bingSearch import search

app = Flask(__name__)

@app.route('/')
def homepage():

	return render_template('homepage.html')

@app.route('/data-result')
def dataoutcome():
	user_input_url = request.args.get("url-input")
	website_url = "https://www." + user_input_url
	data_measure = measure("https://www." + user_input_url) #calling measure() function

	return render_template('data-result.html', website_url = website_url, 
		data_measure = data_measure)

# @app.route('/bingSearchHomepage')
# def bingsearch(str):


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)