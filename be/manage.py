import os

from app import create_app
from ext import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import app.model

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
