from flask import Flask, render_template, send_file
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from flask import Blueprint
from .config import Config
from blog.extensions import cache
from flask import send_from_directory
import os


blueprint = Blueprint('blog', __name__, static_folder='static', template_folder='templates')

try:
    client = ImgurClient(Config.CLIENT_ID, Config.CLIENT_SECRET)
except ImgurClientError as e:
    print(e.error_message, e.status_code)

# Home page


@blueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(blueprint.root_path, 'static'),
                               'favicon.ico', mimetype='Cookie.png')

@blueprint.route('/')
@cache.cached(timeout=50)
def homepage():
    return render_template('homepage.html')

# Locations

@blueprint.route('/<name>')
@cache.cached(timeout=50)
def location(name):

    locations = {
        "london" : "VcG7CLZ",
        "thailand": "NJ3qhK4",
        "bayarea" : "G5aYs7L",
        "chicago" : "WuYSP4B",
        "portland" : "2SDUNao",
        "losangeles" : "tqPQSGb",
        "sandiego" : "G2kP8GY",
        "seattle" : "25wMsrQ",
        "paris" : "WlKdngR",
        "philadelphia" : "AEkStsy",
        "honolulu" : "V3VMK3J",
    }
    
    photos = [x for x in [item.link for item in client.get_album_images(locations[name])] if x.endswith('.jpg')]
    return render_template(name+'.html', photos=photos)

# Resume

@blueprint.route('/resume')
@cache.cached(timeout=50)
def return_pdf():
    return send_file('static/TylerGuoResume.pdf')