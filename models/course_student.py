from app import db

class CourseStudent(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)

	# foreign key
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

	def __init__(self, course_id, student_id):
		self.course_id = course_id
		self.student_id = student_id

def create_course_student(course_id, student_id):
	from models import course, student
	cou = course.get_course(course_id)
	stu = student.get_student(student_id)
	if cou is None or stu is None:
		print(f"[CREATE COURSE STUDENT FAIL] COURSE:{course_id}, STUDENT:{student_id}")
		return False

	try:
		new_course_student = CourseStudent(course_id=course_id, student_id=student_id)
		db.session.add(new_course_student)
		db.session.commit()
		print(f"[CREATE COURSE STUDENT SUCC] COURSE_NAME:{cou.get_course_name()}, STUDENT_NAME:{stu.get_student_name()}")
		return True
	except Exception as e:
		print(f"[CREATE COURSE STUDENT FAIL] COMMIT FAIL")
		db.session.rollback()
		return False

def delete_course_student(course_id, student_id):
	from models import course, student
	cou = course.get_course(course_id)
	stu = student.get_student(student_id)
	if cou is None or stu is None:
		print(f"[DELETE COURSE STUDENT FAIL] COURSE:{course_id}, STUDENT:{student_id}")
		return False

	course_student_model = get_course_student(course_id, student_id)
	if course_student_model:
		try:
			db.session.delete(course_student_model)
			db.session.commit()
			print(f"[DELETE COURSE STUDENT SUCC] COURSE:{course_id}, STUDENT:{student_id}")
			return True
		except Exception as e:
			print(f"[DELETE COURSE STUDENT FAIL] COURSE:{course_id}, STUDENT:{student_id}")
			db.session.rollback()
			return False
	return False

def get_course_student(course_id, student_id):
	return CourseStudent.query.filter_by(course_id=course_id, student_id=student_id).first()

def get_student_ids_by_course(course_id):
	# 查看选择某课程的所有学生
	course_student_models = CourseStudent.query.filter_by(course_id=course_id).all()
	return [course_student_model.student_id for course_student_model in course_student_models]

def get_course_ids_by_student(student_id):
	# 查看某学生选择的所有课程
	course_student_models = CourseStudent.query.filter_by(student_id=student_id).all()
	return [course_student_model.course_id for course_student_model in course_student_models]
