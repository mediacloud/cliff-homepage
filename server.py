import os
import sys
import logging
import json
from flask import Flask, render_template, request

from cliff.api import Cliff

MAX_CHARS = 250 	# limit the amount of text users can send in

app = Flask(__name__)

# setup logging
logging.basicConfig(level=logging.WARN)
log = logging.getLogger('cliff-homepage')
log.info("---------------------------------------------------------------------------")

# set up the api client we will use
if 'CLIFF_URL' in os.environ:
    CLIFF_URL = os.environ['CLIFF_URL']
else:
    log.error("You must set a CLIFF_URL environment variable that points to your server's base url")
    sys.exit()

cliff = Cliff(CLIFF_URL)


# render the homepage
@app.route("/")
def index():
    return render_template('home.html')


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
