import const
from flask import render_template
from flask_login import login_required, current_user
from . import bp

@bp.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@bp.route('/home', methods=['GET'])
@login_required
def home():
	user_type = current_user.get_user_type()
	if user_type == const.UserType.STUDENT.value:
		return render_template('student_space.html')
	elif user_type == const.UserType.TEACHER.value:
		return render_template('teacher_space.html')
	return render_template('error.html')