from . import bp
from blueprints import ensure_student, ensure_teacher
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from .form import TeacherInfoForm, StudentInfoForm

@bp.route('/edit_teacher_info', methods=['GET'])
@login_required
@ensure_teacher
def edit_teacher_info():
	tea = current_user.teacher[0]
	kwargs = {
		'name': tea.name,
	}
	teacher_info_form = TeacherInfoForm(**kwargs)
	return render_template('edit_teacher_info.html', form=teacher_info_form)

@bp.route('/submit_teacher_info', methods=['POST'])
@login_required
@ensure_teacher
def submit_teacher_info():
	teacher_info_form = TeacherInfoForm()
	name = teacher_info_form.name.data

	tea = current_user.teacher[0]
	tea.name = name

	from app import db
	try:
		db.session.commit()
		print(f"[SUBMIT TEACHER INFO SUCC] TEACHER_NAME:{name}")
	except Exception as e:
		print("[SUBMIT TEACHER INFO FAIL]", e)
		db.session.rollback()

	return redirect(url_for('space.teacher_space'))

@bp.route('/edit_student_info', methods=['GET'])
@login_required
@ensure_student
def edit_student_info():
	stu = current_user.student[0]
	kwargs = {
		'name': stu.name,
		'sex': stu.sex,
		'native_place': stu.native_place,
		'political_status': stu.political_status,
		'major': stu.major,
		'address': stu.address,
		'phone': stu.phone
	}
	student_info_form = StudentInfoForm(**kwargs)
	return render_template('edit_student_info.html', form=student_info_form)

@bp.route('/submit_student_info', methods=['POST'])
@login_required
@ensure_student
def submit_student_info():
	student_info_form = StudentInfoForm()
	name = student_info_form.name.data
	sex = student_info_form.sex.data
	native_place = student_info_form.native_place.data
	political_status = student_info_form.political_status.data
	major = student_info_form.major.data
	address = student_info_form.address.data
	phone = student_info_form.phone.data

	stu = current_user.student[0]
	stu.name = name
	stu.sex = sex
	stu.native_place = native_place
	stu.political_status = political_status
	stu.major = major
	stu.address = address
	stu.phone = phone

	from app import db
	try:
		db.session.commit()
		print(f"[SUBMIT STUDENT INFO SUCC] STUDENT_NAME:{name}")
	except Exception as e:
		print("[SUBMIT STUDENT INFO FAIL]", e)
		db.session.rollback()

	return redirect(url_for('space.student_space'))

@bp.route('/teacher_view_student_info/<student_id>')
@login_required
@ensure_teacher
def teacher_view_student_info(student_id):
	from models import student
	stu = student.get_student(student_id)
	if not stu:
		return redirect(url_for('space.teacher_space'))

	return render_template('teacher_view_student_info.html', student=stu)
