from flask import Flask, render_template, send_file
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from flask import Blueprint
from .config import Config
from blog.extensions import cache


blueprint = Blueprint('blog', __name__, template_folder='templates')

try:
    client = ImgurClient(Config.CLIENT_ID, Config.CLIENT_SECRET)
except ImgurClientError as e:
    print(e.error_message, e.status_code)

# Home page

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
    }
    
    photos = [x for x in [item.link for item in client.get_album_images(locations[name])] if x.endswith('.jpg')]
    return render_template(name+'.html', photos=photos)

# Resume

@blueprint.route('/resume')
@cache.cached(timeout=50)
def return_pdf():
    return send_file('static/resume.pdf')