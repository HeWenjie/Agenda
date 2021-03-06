import logging
import const
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

USERNAME_MAX_LENGTH = 20
# consider hash
PASSWORD_MAX_LENGTH = 100
USER_TYPE_MAX_LENGTH = 10

LOG_CREATE_USER_SUCC = "添加用户成功"
LOG_CREATE_USER_FAIL = "添加用户失败"

class User(UserMixin, db.Model):
	# field
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(USERNAME_MAX_LENGTH), unique=True)
	password = db.Column(db.String(PASSWORD_MAX_LENGTH))
	user_type = db.Column(db.String(USER_TYPE_MAX_LENGTH))

	def __init__(self, username, password, user_type):
		self.username = username
		self.password = generate_password_hash(password)
		self.user_type = user_type

	def __repr__(self):
		return f'<User {self.username}>'

	def get_id(self):
		return self.user_id

	def get_password(self):
		return self.password

	def verify_password(self, password):
		return check_password_hash(self.get_password(), password)

	def get_user_type(self):
		return self.user_type

	def is_teacher(self):
		return self.user_type == const.UserType.TEACHER.value

	def is_student(self):
		return self.user_type == const.UserType.STUDENT.value

def load_user(user_id):
	return User.query.get(int(user_id))

def get_user(username):
	return User.query.filter_by(username=username).first()

def create_user(username, password, user_type):
	try:
		new_user = User(username=username, password=password, user_type=user_type)
		db.session.add(new_user)
		db.session.commit()
		logging.info(f"{LOG_CREATE_USER_SUCC}", username=username)
		return new_user
	except Exception as e:
		logging.error(f"{LOG_CREATE_USER_FAIL}", username=username)
		db.session.rollback()
		return None

def verify_user(username, password):
	login_user: User = get_user(username)
	if not login_user:
		return False

	return login_user.verify_password(password)

