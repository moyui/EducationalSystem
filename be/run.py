import os

from app import create_app
from ext import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(port=8888)