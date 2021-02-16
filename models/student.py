from app import db

STUDENT_NAME_MAX_LENGTH = 20

class Student(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(STUDENT_NAME_MAX_LENGTH))

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
