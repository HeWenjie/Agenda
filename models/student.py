from app import db

STUDENT_DEFAULT_MAX_LENGTH = 10
STUDENT_NAME_MAX_LENGTH = 20
STUDENT_SEX_MAX_LENGTH = 10

class Student(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(STUDENT_NAME_MAX_LENGTH))
	sex = db.Column(db.String(STUDENT_SEX_MAX_LENGTH))
	native_place = db.Column(db.String(STUDENT_DEFAULT_MAX_LENGTH))
	political_status = db.Column(db.String(STUDENT_DEFAULT_MAX_LENGTH))
	major = db.Column(db.String(STUDENT_DEFAULT_MAX_LENGTH))
	address = db.Column(db.String(STUDENT_DEFAULT_MAX_LENGTH))
	phone = db.Column(db.String(STUDENT_DEFAULT_MAX_LENGTH))

	# foreign key
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

	# relationship
	user = db.relationship('User', backref='student')

	def __init__(self, user_id):
		self.user_id = user_id

	def get_id(self):
		return self.id

	def get_student_name(self):
		return self.name

def create_student(user_id):
	try:
		new_student = Student(user_id=user_id)
		db.session.add(new_student)
		db.session.commit()
		return True
	except Exception as e:
		db.session.rollback()
		return False

def get_student(student_id):
	return Student.query.get(student_id)
