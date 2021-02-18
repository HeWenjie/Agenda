from functools import wraps
from flask_login import current_user

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