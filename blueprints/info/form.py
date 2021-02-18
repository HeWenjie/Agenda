import const
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TeacherInfoForm(FlaskForm):
	name = StringField(label='教师姓名', validators=[DataRequired()])
	submit = SubmitField('提交')

class StudentInfoForm(FlaskForm):
	# student_id = StringField(label='学号', validators=[DataRequired()])
	name = StringField(label='学生姓名', validators=[DataRequired()])
	sex = SelectField(label='性别', validators=[DataRequired()], choices=['男', '女'])
	native_place = StringField(label='籍贯', validators=[DataRequired()])
	political_status = StringField(label='政治面貌', validators=[DataRequired()])
	major = StringField(label='专业', validators=[DataRequired()])
	address = StringField(label='通讯地址')
	phone = StringField(label='联系电话')
	submit = SubmitField('提交')
