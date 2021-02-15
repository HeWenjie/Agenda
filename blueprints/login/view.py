from flask_wtf import FlaskForm
from wtforms import (
	StringField,
	PasswordField,
	SubmitField,
)
from wtforms.validators import  (
	DataRequired,
	EqualTo,
)

class LoginForm(FlaskForm):
	username = StringField(label='用户名', validators=[DataRequired()])
	password = PasswordField(label='密码', validators=[DataRequired()])
	submit = SubmitField(label='登录')

class RegisterForm(FlaskForm):
	username = StringField(label='用户名', validators=[DataRequired()])
	password = PasswordField(label='密码', validators=[DataRequired()])
	confirm_password = PasswordField(
		label='确认密码',
		validators=[DataRequired(), EqualTo('password', message='密码不一致')])
	submit = SubmitField(label='注册')
