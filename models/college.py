from app import db

COLLEGE_NAME_MAX_LENGTH = 20

class College(db.Model):
	# field
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(COLLEGE_NAME_MAX_LENGTH), unique=True)

	# relationship
	students = db.relationship('Student', backref='college')
	teachers = db.relationship('Teacher', backref='college')