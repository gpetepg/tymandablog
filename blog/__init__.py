from flask import Flask
from blog.extensions import db, migrate
import blog.config as configure
import os


def create_app(config=None):
    # create app
    app = Flask(__name__)

    # set config
    if config == 'testing':
        app.config.from_object(configure.TestingConfig)
    elif config == 'development':
        app.config.from_object(configure.DevelopmentConfig)
    elif config == 'production':
        app.config.from_object(configure.ProductionConfig)
    else:
        raise ValueError('Incorrect configuration')

    # extensions
    # db.init_app(app)
    # migrate.init_app(app, db)

    # blueprints
    from .routes import blueprint as blog

    app.register_blueprint(blog, url_prefix='')

    return app