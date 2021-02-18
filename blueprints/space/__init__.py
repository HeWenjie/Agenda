from flask import Blueprint

bp = Blueprint('space', __name__, template_folder='templates', static_folder='static')

from . import view
