import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.reddit.com/r/news/"
headers = {'User-Agent':'Mozilla/5.0'}
def scrape(db):
	html = requests.get(url,headers=headers).content
	soup = BeautifulSoup(html,"html.parser")
	conn = db.connect()
	if conn is not None:
		for i in reversed(soup.find_all('a', class_='SQnoC3ObvgnGjWt90zD9Z')): 
			try :
				href = 'https://www.reddit.com'+i['href']
				c = conn.cursor()
				c.execute("INSERT INTO content_agg(source,title,url) VALUES('reddit', ?, ?)",(i.text.strip(), href))
			except sqlite3.IntegrityError as e:
				pass
			except Exception as e:
				print("Error : ", e)
				return False
		conn.commit()
		conn.close()
		return True
	else :
		return False
