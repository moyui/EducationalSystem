from flask import Blueprint

shop = Blueprint('shop', __name__)

from . import route