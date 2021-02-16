import const
from flask_wtf import FlaskForm
from wtforms import (
	StringField,
	SubmitField,
)
from wtforms.validators import  (
	DataRequired,
	Length,
)

class CreateCourseForm(FlaskForm):
	course_name = StringField(
		label='课程名',
		validators=[DataRequired(),
					Length(const.COURSE_NAME_MIN_LENGTH, const.COURSE_NAME_MAX_LENGTH)])
	submit = SubmitField(label='提交')
