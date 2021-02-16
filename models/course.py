import const
from app import db

class Course(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	course_name = db.Column(db.String(const.COURSE_NAME_MAX_LENGTH))

	# foreign key
	teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

	def __init__(self, course_name, teacher_id):
		self.course_name = course_name
		self.teacher_id = teacher_id

	def get_course_name(self):
		return self.course_name

def create_course(teacher_id, course_name):
	try:
		new_course = Course(course_name=course_name, teacher_id=teacher_id)
		db.session.add(new_course)
		db.session.commit()
		print(f"[CREATE COURSE SUCC] COURSE_NAME:{course_name}")
		return True
	except Exception as e:
		print(f"[CREATE COURSE FAIL] TEACHER_ID:{teacher_id}, COURSE_NAME:{course_name}", e)
		db.session.rollback()
		return False

def delete_course(course_id):
	course = get_course(course_id)
	if course:
		try:
			db.session.delete(course)
			db.session.commit()
			return True
		except Exception as e:
			db.session.rollback()
			return False
	return False

def get_all_courses():
	return Course.query.all()

def get_course(course_id):
	return Course.query.get(course_id)
