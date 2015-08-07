from flask import Flask, render_template, request

from measure import measure #from measure.py file, import measure() function

from bingSearch import search # from bingSearch import search

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

@app.route('/bingSearchHomepage')
def bingsearch():

	return render_template('bingsearchhome.html')

@app.route('/bingSearchResult')
def bingResult():
	bing_input = request.args.get("bing_input")
	search_input = str(bing_input)
	search_list = search(search_input)
	output_search = []

	for s in search_list:
		output_search += s.title, s.url

	output_search_split = " "
	for o in output_search:
		output_search_split += o.split(",")[0] + " "

		
	return render_template('bingresult.html', bing_input = bing_input, 
		output_search = output_search_split)


# search_list = search('puppy')
# output_search = ""
# for search in search_list:
# 	output_search = search.title, search.url
# 	print output_search
# self.title:         title of the result
# self.url:           the url of the result
# self.description:   description for the result
# self.id:            bing id for the page


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)