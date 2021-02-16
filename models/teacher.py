from app import db

TEACHER_NAME_MAX_LENGTH = 20

class Teacher(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(TEACHER_NAME_MAX_LENGTH))

	# foreign key
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

	# relationship
	courses = db.relationship('Course', backref='teacher')

	def __init__(self, user_id):
		self.user_id = user_id

	def get_id(self):
		return self.id

def create_teacher(user_id):
	try:
		new_teacher = Teacher(user_id=user_id)
		db.session.add(new_teacher)
		db.session.commit()
		return True
	except Exception as e:
		db.session.rollback()
		return False
