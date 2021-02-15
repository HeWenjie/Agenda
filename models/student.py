from app import db

STUDENT_NAME_MAX_LENGTH = 20

class Student(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(STUDENT_NAME_MAX_LENGTH))

	# foreign key
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

	def __init__(self, user_id):
		self.user_id = user_id

def create_student(user_id):
	try:
		new_student = Student(user_id=user_id)
		db.session.add(new_student)
		db.session.commit()
		return True
	except Exception as e:
		db.session.rollback()
		return False
