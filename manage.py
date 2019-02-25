from blog import create_app
from flask_script import Manager
from flask_migrate impoirt Migrate, MigrateCommand

manager = Manager(create_app(config='testing'))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()