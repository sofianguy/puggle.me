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
	# bing_input = request.args.get("bing_input")
	# search_input = str(bing_input)
	# search_list = search(search_input)
	# output_search = []

	# for s in search_list:
	# 	print "measure", s.url
	# 	output_search += s.title, s.url, measure(s.url)

	# output_search_split = " "
	# for o in output_search:
	# 	output_search_split += o.split(",")[0] + " "
	# 	print type(output_search_split) #unicode type
	page_data_structure = [
		# 4 object go here, 1 for each page
		{
		'title': 'PuppyFind.com - Official Site', 
		'url': 'https://www.puppyfind.com', 
		'description': 'Directory of dog breeders with puppies for sale and dogs for adoption. Find the right breed, and the perfect puppy at PuppyFind.com.',
		'data': '800kb'
		},

		{
		'title': 'Puppy - Wikipedia, the free encyclopedia',
		'url': 'https://en.wikipedia.org/wiki/Puppy',
		'description': 'A puppy is a juvenile dog. Some puppies can weigh ',
		'data': '750kb'
		},

		{
		'title': 'The Daily Puppy - Official Site',
		'url': 'https://www.dailypuppy.com',
		'description': 'Find cute puppy pictures and videos. Learn how to care for and train puppies. Submit your puppy to be the daily puppy, create profiles for you and your dogs and share ...',
		'data': '700kb'
		},

		{
		'title': 'New Puppy Care Tips: Puppy 101 | PetSmart',
		'url': 'https://pets.petsmart.com/guides/puppy-center',
		'description': 'Our puppy care center has everything a new pet parent needs! From how-to videos, new puppy checklist, food & nutrition articles, potty training tips, grooming and ...',
		'data': '600kb'
		}
	]
		
	return render_template('bingresult.html', page_data_structure = page_data_structure)


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