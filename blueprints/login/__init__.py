import const
from flask import (
	Blueprint,
	render_template,
	request,
	redirect,
	url_for,
	flash,
)
from .view import (
	LoginForm,
	RegisterForm,
)
from flask_login import (
	login_user,
	logout_user,
	login_required,
)

MSG_USER_EXIST = '用户已存在'
MSG_USER_NO_EXIST = '用户不存在'
MSG_DATA_INVALID = '输入有误'
MSG_VERIFY_PWD_FAIL = '密码不正确'

bp = Blueprint('login', __name__, template_folder='templates', static_folder='static')

@bp.route('/login', methods=['GET', 'POST'])
def login():
	login_form = LoginForm()
	if request.method == 'POST':
		username = login_form.username.data
		password = login_form.password.data
		if login_form.validate_on_submit():
			from models import user
			_user = user.get_user(username)
			if not _user:
				flash(MSG_USER_NO_EXIST)
				return render_template('login.html', form=login_form)

			if _user.verify_password(password):
				login_user(_user)
				return redirect(url_for('home.index'))
			else:
				flash(MSG_VERIFY_PWD_FAIL)
				return render_template('login.html', form=login_form)
		else:
			flash(MSG_DATA_INVALID)
			return render_template('login.html', form=login_form)
	else:
		return render_template('login.html', form=login_form)

@bp.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
	register_form = RegisterForm()
	if request.method == 'POST':
		if register_form.validate_on_submit():
			from models import user
			username = register_form.username.data
			password = register_form.password.data
			user_type = register_form.user_type.data
			if user.get_user(username):
				flash(MSG_USER_EXIST)
				return render_template('register.html', form=register_form)
			else:
				new_user = user.create_user(username=username, password=password, user_type=user_type)
				if new_user:
					if user_type == const.UserType.STUDENT.value:
						from models import student
						student.create_student(new_user.get_id())
					else:
						from models import teacher
						teacher.create_teacher(new_user.get_id())
				return render_template('index.html', form=register_form)
		else:
			flash(MSG_DATA_INVALID)
			return render_template('register.html', form=register_form)
	else:
		return render_template('register.html', form=register_form)
