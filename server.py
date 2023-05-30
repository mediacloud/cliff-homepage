import logging
import json
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

from cliff.api import Cliff

VERSION = "2.6.1"

MAX_CHARS = 250 	# limit the amount of text users can send in

load_dotenv()  # set environment variables from .env file if available

app = Flask(__name__)

# setup logging
logging.basicConfig(level=logging.WARN)
log = logging.getLogger(__file__)
log.info("---------------------------------------------------------------------------")


# set up the api client we will use
CLIFF_URL = os.environ.get("CLIFF_URL", "http://localhost:8080")
cliff = Cliff(CLIFF_URL)


# render the homepage
@app.route("/")
def index():
    return render_template('home.html', version=VERSION)


# return json results from CLIFF 
@app.route("/process", methods=['POST'])
def geoparse():
    text = request.form['text']
    language = request.form['language']
    demonyms = request.form['demonyms'] == 'true'
    results = cliff.parse_text(text[0:MAX_CHARS], demonyms, language)
    return json.dumps(results)


if __name__ == "__main__":
    app.debug = True
    app.run()
