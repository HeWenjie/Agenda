from . import bp
from . import ensure_teacher, ensure_student
from .form import CreateCourseForm
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

@bp.route('/teacher_space')
@login_required
def teacher_space():
	return render_template('teacher_space.html')

@bp.route('/student_space')
@login_required
def student_space():
	return render_template('student_space.html')

@bp.route('/create_course', methods=['GET', 'POST'])
@login_required
@ensure_teacher
def create_course():
	create_course_form = CreateCourseForm()
	if request.method == 'POST':
		course_name = create_course_form.course_name.data
		teacher_id = current_user.teacher[0].get_id()
		from models import course
		course.create_course(teacher_id, course_name)
		return redirect(url_for('space.teacher_space'))
	else:
		return render_template('create_course.html', form=create_course_form)

@bp.route('/delete_course/<course_id>')
@login_required
@ensure_student
def delete_course(course_id):
	from models import course_student
	student_id = current_user.student[0].get_id()
	course_student.delete_course_student(course_id, student_id)
	return redirect(url_for('space.view_selected_course'))

@bp.route('/view_all_course', methods=['GET'])
@login_required
@ensure_student
def view_all_course():
	from models import course
	courses = course.get_all_courses()
	return render_template('view_all_course.html', courses=courses)

@bp.route('/view_selected_course', methods=['GET'])
@login_required
@ensure_student
def view_selected_course():
	from models import course_student, course
	student_id = current_user.student[0].get_id()
	course_ids = course_student.get_course_ids_by_student(student_id)
	courses = []
	for course_id in course_ids:
		cou = course.get_course(course_id)
		if cou is None:
			continue
		courses.append(cou)
	return render_template('view_selected_course.html', courses=courses)

@bp.route('/choose_course/<course_id>')
@login_required
@ensure_student
def choose_course(course_id):
	from models import course_student
	student_id = current_user.student[0].get_id()
	course_student.create_course_student(course_id, student_id)
	return redirect(url_for('space.student_space'))
