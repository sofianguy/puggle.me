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
	# print search_list

	page_data_structure_2 = []

	for s in search_list:
		page_data_structure_2.append({
		'title': s.title,
		'url': s.url,
		'description': s.description,
		'data': measure(s.url)
		})

	return render_template('bingresult.html', page_data_structure = page_data_structure_2)


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