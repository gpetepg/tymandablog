from flask import Flask, render_template, send_file
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from flask import Blueprint
from .config import Config


blueprint = Blueprint('blog', __name__, template_folder='templates')

try:
    client = ImgurClient(Config.CLIENT_ID, Config.CLIENT_SECRET)
except ImgurClientError as e:
    print(e.error_message, e.status_code)

# Home page

@blueprint.route('/')
def homepage():
    return render_template('homepage.html')

# Locations

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
    "philly" : "AEkStsy'",
}

@blueprint.route('/<name>')
def location(name):
    photos = [x for x in [item.link for item in client.get_album_images(locations[f'{name}'])] if '.jpg' in x]
    return render_template(f'{name}.html', photos=photos)

# Resume

@blueprint.route('/resume')
def return_pdf():
    return send_file('static/resume.pdf')