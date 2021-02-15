from app import db

TEACHER_NAME_MAX_LENGTH = 20

class Teacher(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(TEACHER_NAME_MAX_LENGTH))

	# foreign key
	college_id = db.Column(db.Integer, db.ForeignKey('college.id'))
