from flask import Flask
from .config import config
from ext import db
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api')
    from .course import course as course_blueprint
    app.register_blueprint(course_blueprint, url_prefix='/api')
    from .shop import shop as shop_blueprint
    app.register_blueprint(shop_blueprint, url_prefix='/api')
    from .video import video as video_blueprint
    app.register_blueprint(video_blueprint, url_prefix='/api')
    from .comment import comment as comment_blueprint
    app.register_blueprint(comment_blueprint, url_prefix='/api')
    return app
