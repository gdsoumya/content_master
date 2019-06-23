from flask import Flask, render_template, redirect
from db_handler import db
import ScrapeJob as sj
import threading

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def home():
	content = sj.getContent()
	if content is None:
		return "FETCHING DATA PLEASE TRY AGAIN LATER !"
	return render_template('index.html', content = content)

@app.route('/readmore/<source>', methods = ["GET"])
def readmore(source):
	content = sj.getContentForSource(source)
	if content is None:
		return redirect('/404')
	return render_template('readmore.html', content = content)


if __name__ == '__main__':
	
	#Strat ScrapeJob as a background job in a new thread 
	t1 = threading.Thread(target=sj.scrapeStart) 
	t1.daemon = True
	t1.start() 

	# Start Flask SERVER
	app.run()