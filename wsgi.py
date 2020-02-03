"""For deployment"""

from blog import create_app

app = create_app(config='production')

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()
