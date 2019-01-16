import logging
import json
import config
from flask import Flask, render_template, request

from cliff.api import Cliff

VERSION = "2.3.0"

MAX_CHARS = 250 	# limit the amount of text users can send in

app = Flask(__name__)

# setup logging
logging.basicConfig(level=logging.WARN)
log = logging.getLogger(__file__)
log.info("---------------------------------------------------------------------------")

app_config = config.get_default_config()

# set up the api client we will use
CLIFF_URL = app_config.get('CLIFF_URL')
cliff = Cliff(CLIFF_URL)


# render the homepage
@app.route("/")
def index():
    return render_template('home.html', version=VERSION)


# return json results from CLIFF 
@app.route("/process",methods=['POST'])
def geoparse():
    text = request.form['text']
    demonyms = request.form['demonyms'] == 'true'
    results = cliff.parse_text(text[0:MAX_CHARS], demonyms)
    return json.dumps(results)


if __name__ == "__main__":
    app.debug = True
    app.run()
