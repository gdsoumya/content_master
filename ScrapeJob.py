from db_handler import db
import time
from scraper import reutersIN, bbc, theverge, techmeme, techcrunch, reddit

source = ['reddit', 'reutersIN', 'techcrunch', 'theverge', 'techmeme', 'bbc'] 
name = ['Reddit','Reuters India','TechCrunch','The Verge', 'Techmeme', 'BBC']

def scrapeAll():
	if not reutersIN.scrape(db):
		print("ERROR : REUTERS IN SCRAPE ERROR")
	if not  bbc.scrape(db) :
		print("ERROR : BBC SCRAPE ERROR")
	if not  theverge.scrape(db) :
		print("ERROR : THE VERGE SCRAPE ERROR")
	if not  techmeme.scrape(db) :
		print("ERROR : TECHMEME SCRAPE ERROR")
	if not  techcrunch.scrape(db) :
		print("ERROR : TECHCRUNCH SCRAPE ERROR")
	if not  reddit.scrape(db):
		print("ERROR : REDDIT SCRAPE ERROR")
	print("SCRAPING COMPLETE")

def getContent():
	content = {}
	conn = db.connect()
	c = conn.cursor()
	# source = c.execute('Select distinct source from content_agg');
	# source = [i[0] for i in source]
	for j,i in enumerate(source) :
		z = c.execute("Select * from content_agg where source='{}' order by rowid desc;".format(i));  
		content[name[j]] = z.fetchall()
		if content[name[j]] ==[]:
			conn.close()
			return None
	conn.close()
	return content

def getContentForSource(s):
	if s in source :
		i = source.index(s)
		content = {}
		conn = db.connect()
		c = conn.cursor()
		z = c.execute("Select * from content_agg where source='{}' order by rowid desc;".format(s));  
		content[name[i]] = z.fetchall()
		if content[name[j]] ==[]:
			conn.close()
			return None
		conn.close()
		return content
	else:
		return None

def scrapeStart():
	while True:
		scrapeAll()
		time.sleep(3600) # Content Updated every 1hr

# Running ScrapeJob.py directly executes scrapeAll() once
if __name__ == '__main__':
	scrapeAll()

