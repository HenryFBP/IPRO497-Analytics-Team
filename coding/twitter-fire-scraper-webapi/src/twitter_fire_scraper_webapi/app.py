import os
from flask import Flask, request, render_template, jsonify, url_for

app = Flask(__name__, static_url_path="/static")


@app.route('/info', methods=['GET'])
def info(): # function: check webapi is running or not
    return "twitter-fire-scraper-webapi"

@app.route('/')
def index():
    return jsonify({'json': 'hacked'})

@app.route('/add/<int:x>/<int:y>', methods=['GET'])
def add_numbers(x, y):
    return str(x+y)

@app.route('/scraper/scrape?terms=<str:term>', methods=['GET'])
from twitter_fire_scraper.scraper import Scraper
Scraper.scrape(terms=term)

### Task to be completed:
# https://github.com/raaraa/IPRO497-Analytics-Team/tree/master/Documents/spring-break-tasks

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3620))

    app.run(host="127.0.0.1", port=port, debug=True)
