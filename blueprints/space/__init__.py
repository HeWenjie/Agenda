from functools import wraps
from flask import Blueprint
from flask_login import current_user

bp = Blueprint('space', __name__, template_folder='templates', static_folder='static')

def ensure_teacher(func):
	@wraps(func)
	def wrap_func(*args, **kwargs):
		if not current_user.is_teacher():
			return None
		return func(*args, **kwargs)
	return wrap_func

def ensure_student(func):
	@wraps(func)
	def wrap_func(*args, **kwargs):
		if not current_user.is_student():
			return None
		return func(*args, **kwargs)
	return wrap_func


from . import view