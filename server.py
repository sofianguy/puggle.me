from flask import Flask, render_template, request

from measure import measure #from measure.py file, import measure() function

app = Flask(__name__)

@app.route('/')
def homepage():

	return render_template('homepage.html')

@app.route('/data-result')
def dataoutcome():
	data_outcome = request.args.get("URL-input")
	data_measure = measure("https://" + data_outcome)

	return render_template('data-result.html', data_measure = data_measure)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)