from flask import Blueprint

bp = Blueprint('passport', __name__, template_folder='templates', static_folder='static')

from . import view
