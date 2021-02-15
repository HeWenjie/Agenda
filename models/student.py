from app import db

STUDENT_NAME_MAX_LENGTH = 20

class Student(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(STUDENT_NAME_MAX_LENGTH))

	# foreign key
	college_id = db.Column(db.Integer, db.ForeignKey('college.id'))
