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

@blueprint.route('/london')
def london():
    london_photos = [x for x in [item.link for item in client.get_album_images('VcG7CLZ')] if '.jpg' in x]
    return render_template('london.html', london_photos=london_photos)


@blueprint.route('/thailand')
def thailand():
    thai_photos = [x for x in [item.link for item in client.get_album_images('NJ3qhK4')] if '.jpg' in x]
    return render_template('thailand.html', thai_photos=thai_photos)


@blueprint.route('/bayarea') 
def bayarea():
    bay_photos = [x for x in [item.link for item in client.get_album_images('G5aYs7L')] if '.jpg' in x]
    return render_template('bayarea.html', bay_photos=bay_photos)


@blueprint.route('/chicago')
def chicago():
    chicago_photos = [x for x in [item.link for item in client.get_album_images('WuYSP4B')] if '.jpg' in x]
    return render_template('chicago.html', chicago_photos=chicago_photos)


@blueprint.route('/portland')
def portland():
    portland_photos = [x for x in [item.link for item in client.get_album_images('2SDUNao')] if '.jpg' in x]
    return render_template('portland.html', portland_photos=portland_photos)


@blueprint.route('/losangeles')
def losangeles():
    losangeles_photos = [x for x in [item.link for item in client.get_album_images('tqPQSGb')] if '.jpg' in x]
    return render_template('losangeles.html', losangeles_photos=losangeles_photos)


@blueprint.route('/sandiego')
def sandiego():
    sandiego_photos = [x for x in [item.link for item in client.get_album_images('G2kP8GY')] if '.jpg' in x]
    return render_template('sandiego.html', sandiego_photos=sandiego_photos)


@blueprint.route('/seattle')
def seattle():
    seattle_photos = [x for x in [item.link for item in client.get_album_images('25wMsrQ')] if '.jpg' in x]
    return render_template('seattle.html', seattle_photos=seattle_photos)


@blueprint.route('/paris')
def paris():
    paris_photos = [x for x in [item.link for item in client.get_album_images('WlKdngR')] if '.jpg' in x]
    return render_template('paris.html', paris_photos=paris_photos)


@blueprint.route('/philadelphia')
def philadelphia():
    philadelphia_photos = [x for x in [item.link for item in client.get_album_images('AEkStsy')] if '.jpg' in x]
    return render_template('philadelphia.html', philadelphia_photos=philadelphia_photos)

# Resume

@blueprint.route('/resume')
def return_pdf():
    return send_file('static/resume.pdf')