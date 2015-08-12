from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Search(db.Model):

	__tablename__ = "Searches"

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	search = db.Column(db.Text(), nullable=False)
	datetime = db.Column(db.Integer, nullable=False)

	results = db.relationship('Result', backref=db.backref('search'))
#backref is: on other table, what you call this table: "search"
#backref is not case sensitive(table name)

class Website(db.Model):

	__tablename__ = "Websites"

	url = db.Column(db.Text(), nullable=False, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String(200), nullable=False)
	
	results = db.relationship('Result', backref=db.backref('website'))

class Result(db.Model):

	__tablename__ = "Results"

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	website_id = db.Column(db.Text(), ForeignKey('Website.url'), nullable=False)
	search_id = db.Column(db.Integer, ForeignKey('Search.id'), nullable=False)
	size = db.Column(db.Integer, nullable=False)

# Helper functions
def connect_to_db(app):
	"""Connect the database to our Flask app."""

	# Configure to use our SQLite database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
	app.config['SQLALCHEMY_ECHO'] = True
	db.app = app
	db.init_app(app)


if __name__ == "__main__":
	# As a convenience, if we run this module interactively, it will leave
	# you in a state of being able to work with the database directly.

	# So that we can use Flask-SQLAlchemy, we'll make a Flask app
	from flask import Flask
	app = Flask(__name__)

	connect_to_db(app)
	print "Connected to DB."