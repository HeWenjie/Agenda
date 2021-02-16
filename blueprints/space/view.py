from . import bp
from . import ensure_teacher
from .form import CreateCourseForm
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

@bp.route('/create_course', methods=['GET', 'POST'])
@login_required
@ensure_teacher
def create_course():
	create_course_form = CreateCourseForm()
	if request.method == 'POST':
		course_name = create_course_form.course_name.data
		teacher_id = current_user.get_id()
		from models import course
		course.create_course(teacher_id, course_name)
		return redirect(url_for('space.teacher_space'))
	else:
		return render_template('create_course.html', form=create_course_form)

@bp.route('/teacher_space')
@login_required
def teacher_space():
	return render_template('teacher_space.html')

@bp.route('/student_space')
@login_required
def student_space():
	return render_template('student_space.html')
