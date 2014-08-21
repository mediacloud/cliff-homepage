import os, sys, time, logging, ConfigParser, json
from flask import Flask, render_template, request
from mediameter.cliff import Cliff

MAX_CHARS = 250 	# limit the amount of text users can send in

app = Flask(__name__)

# setup logging
logging.basicConfig(filename='/var/log/cliff-homepage.log',level=logging.DEBUG)
log = logging.getLogger('cliff-homepage')
log.info("---------------------------------------------------------------------------")

# load config file
current_dir = os.path.dirname(os.path.abspath(__file__))
config = ConfigParser.ConfigParser()
config.read(current_dir+'/cliff.config')
cliff = Cliff( config.get('cliff','host'), config.get('cliff','port') )

# render the homepage
@app.route("/")
def index():
    return render_template('home.html')

# return json results from CLIFF 
@app.route("/process",methods=['POST'])
def geoparse():
    text = request.form['text']
    demonyms = request.form['demonyms']=='true'
    results = cliff.parseText(text[0:MAX_CHARS],demonyms)
    return json.dumps(results)

if __name__ == "__main__":
    app.debug = True
    app.run()
