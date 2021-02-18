from flask import Blueprint

bp = Blueprint('info', __name__, template_folder='templates', static_folder='static')

from . import view
