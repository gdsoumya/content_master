# Content Master

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   <img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python"> <a href='https://github.com/gdsoumya' target='_blank'><img src='https://img.shields.io/github/followers/gdsoumya.svg?label=Folow&style=social'></a><a href="https://twitter.com/intent/tweet?text=Check+out+this+awesome+Github+Repo+for+a+Content Aggregator, it collects content from different websites and organizes everything in one place.&url=https%3A%2F%2Fgithub.com%2Fgdsoumya%2Fcontent_master&hashtags=twitter%2Ccontent_aggregator%2Cgithub&original_referer=http%3A%2F%2Fgithub.com%2F&tw_p=tweetbutton" target="_blank">
  <img src="http://jpillora.com/github-twitter-button/img/tweet.png"
       alt="tweet button" title="Check out this awesome Github Repo for a Twitter Bot, it can auto tweet posts using RSS Feed links."></img>
</a>

Content Master is a content aggregator that collects content from different sources, organizes them and puts them in one place for consumption.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

**Content Master** requires [ **Python (> Python 3.6)**](https://www.python.org/) .

### Getting the project.

```sh
$ git clone https://github.com/gdsoumya/content_master.git
or 
Download and extract the Zip-File
```
### Setting up Virtual Environemt
Setting up a virtual environment would be better for both development and normal execution purposes.
```sh
$ cd content_master
$ python -m virtualenv env
$ source env/bin/activate
 or (Windows machine)
$ .\env\Scripts\activate
```
### Installing Dependencies
The Project has a few dependencies which can be installed by running.
```sh
$ pip install -r dependencies.txt 
```
## Starting the Server
To start the Flask server run
```sh
$ python server.py
```
A Flask development server will be initialized at http://127.0.0.1:5000/

### Warnings 
A possible warning that one might get is :

**WARNING: Do not use the development server in a production environment.**

This warning is displayed because currently a Flask Development Server is running but the default environment of Flask is set to Production, to remove this warning change the FLASK_ENV environment variable.
<br>***Setting environment to development automatically sets the debugger on.**
```sh
$ export FLASK_ENV=development
or (Windows machine)
$ set FLASK_ENV=development
```

## Errors and Debugging options
The server by default does not start in debugger mode but to initialize debugger mode change the last line of the '[server.py](https://github.com/gdsoumya/content_master/blob/master/server.py)' file to :
```python
app.run() -> app.run(debug=True)
```
Most errors will be logged to the console and can be referenced later for debugging.
## Packages Used
- **[Requests](https://2.python-requests.org/en/master/)** : For fetching the source websites.
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** : For scraping the source websites.
- **[Flask](http://flask.pocoo.org/)** : For hosting the web interface.

## Author
-   **Soumya Ghosh Dastidar**

## Contributting
Any contribution/suggestions are welcomed.
