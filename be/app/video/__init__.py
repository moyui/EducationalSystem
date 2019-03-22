from flask import Blueprint

video = Blueprint('video', __name__)

from . import route