import os, sys, time, logging, ConfigParser, json
from flask import Flask, render_template, request
from flask.json import jsonify 
from mediameter.cliff import Cliff

app = Flask(__name__)

# setup logging
logging.basicConfig(filename='/var/log/cliff-homepage.log',level=logging.DEBUG)
log = logging.getLogger('cliff-homepage')
log.info("---------------------------------------------------------------------------")

# load config file
current_dir = os.path.dirname(os.path.abspath(__file__))
config = ConfigParser.ConfigParser()
config.read(current_dir+'/cliff.config')
cliff = Cliff( config.get('cliff','host'),config.get('cliff','port') )

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/process",methods=['POST'])
def geoparse():
    text = request.form['text']
    results = cliff.query(text)
    return jsonify(results)

if __name__ == "__main__":
    app.debug = True
    app.run()
