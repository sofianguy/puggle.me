from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bing(db.Model):

	__tablename__ = "Bings"

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String(200), nullable=False)
	data = db.Column(db.Integer, nullable=False)
	datetime = db.Column(db.Integer, nullable=False)

	websites = db.relationship('Website',
		backref=db.backref('bings'), secondary='BingWebsites')
#backref is: on other table, what you call this table: "Bings"
#backref is not case sensitive(table name)

class Website(db.Model):

	__tablename__ = "Websites"

	url = db.Column(db.Text(), nullable=False, primary_key=True)
	data = db.Column(db.Integer, nullable=False)

class BingWebsite(db.Model):

	__tablename__ = "BingWebsites"

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	url = db.Column(db.Text(), ForeignKey('Websites'), nullable=False)
	bing_id = db.Column(db.Integer, ForeignKey('Bings'), nullable=False)


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