from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from blueprints import home, passport, space

app = Flask(__name__)
# secret_key
app.secret_key = '47ea9c5e'
# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hewenjie@localhost:3306/agenda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# register_blueprint
app.register_blueprint(home.bp, url_prefix='/')
app.register_blueprint(passport.bp, url_prefix='/passport')
app.register_blueprint(space.bp, url_prefix='/space')

db = SQLAlchemy(app)
login_manager = LoginManager(app)

# clear table
from models import user, student, teacher, course, course_student
# db.drop_all()
# db.create_all()

login_manager.login_view = 'passport.login'
login_manager.login_message = '你必须登陆后才能访问该页面'
login_manager.login_message_category = "info"
login_manager.user_loader(user.load_user)
