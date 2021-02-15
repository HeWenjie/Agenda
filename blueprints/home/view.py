from flask_wtf import FlaskForm
from wtforms import (
	StringField,
	SelectField,
	DateField,
	SubmitField,
)
from wtforms.validators import  (
	DataRequired,
)

class InfoForm(FlaskForm):
	name = StringField(label='姓名', validators=[DataRequired()])
	sex = SelectField(label='性别', validators=[DataRequired()], choices=['男', '女'])
	birthday = DateField(label='出生日期', validators=[DataRequired()])
	nation = StringField(label='民族', validators=[DataRequired()])
	address = StringField(label='家庭地址', validators=[DataRequired()])
	phone = StringField(label='联系电话', validators=[DataRequired()])
	submit = SubmitField(label='提交')
