from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from app.search.justwatch import JustWatch


# configuration
DEBUG = True
STATIC_DIR = '../dist'

# instantiate the app
app = Flask(__name__, static_folder=STATIC_DIR)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Web application
@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory('%s/js' % STATIC_DIR, filename)

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('%s/css' % STATIC_DIR, filename)

@app.route('/img/<path:filename>')
def send_img(filename):
    return send_from_directory('%s/img' % STATIC_DIR, filename)

# Api
@app.route('/search/tv/<query>', methods=['GET'])
def search_tv(query):
    resp = JustWatch.search_query(query=query)
    return jsonify(resp)
