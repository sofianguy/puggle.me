# puggle.me
Puggle.me helps people with limited internet connectivity find data-plan friendly websites. A great deal of the modern web is inaccessible to people with limited data plans. Puggle.me is a lightweight Bing-powered search that shows the size of each resultant link. Users with extremely limited plans can also receive search results via SMS.

*puggle.me homepage*
![puggle.me homepage](http://i.imgur.com/8five6N.png)

*puggle.me results page*
![puggle.me results page](http://i.imgur.com/qbnmlhp.png)

###How is puggle.me lightweight?
* Minimal webpage design (i.e., by not using Bootstrap)
* Opens websites and scans webpage on the server so that users don’t have to use their data to find out how big a website is
* Puggle.me only shows the results rendered from website scan processes from the server. This is to avoid making puggle.me’s file sizes larger than it has to be. 

###Technologies Used
PhantomJS, SQL Alchemy, SQLite, Flask, Jinja, JavaScript, Python, HTML, CSS, Bing Search API, Twilio API

###Features
*Current*
- [x] PhantomJS opens up website and adds up total file sizes
- [x] Python wrapper function using subprocess (Popen and PIPE)
- [x] Processes run in parallel scanning multiple websites at the same time (multi-thread)
- [x] User can receive search results from SMS (Twilio API)
- [x] Cache search results to database (SQLite)
- [x] 9 second timeout for SMS input processes
- [x] 20 second timeout for web input processes

*Future*
- [ ] Deploy app on Heroku
- [ ] Graph to show breakdown of each website’s components (e.g., images, CSS, JS, etc)
- [ ] “Random button” to render cached search results
- [ ] Average data size for websites
- [ ] Write program to load process results faster
- [ ] Show cost of loading each website, according to individual data plans

###Structure
#####dataMeasure.js 
Opens website and scans website file sizes

#####measure.py
Python wrapper function - wraps dataMeasure.js function in a Python function called in server.py

#####model.py
Sets up SQLite database for caching website results

#####server.py
Core Flask app - queries database for caching results and lists routes

#####bingSearch.py
Used Bing Search API for search engine

#####twilio-message.py
Used Twilio API for text messaging
