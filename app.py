from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from blueprints import (
	login,
	home,
)

app = Flask(__name__)
# secret_key
app.secret_key = '47ea9c5e'
# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hewenjie@localhost:3306/agenda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# register_blueprint
app.register_blueprint(login.bp, url_prefix='/login')
app.register_blueprint(home.bp, url_prefix='/home')

login_manager = LoginManager(app)
login_manager.login_view = 'login.login'
login_manager.login_message = '你必须登陆后才能访问该页面'
login_manager.login_message_category = "info"

db = SQLAlchemy(app)
from models import user
db.drop_all()
db.create_all()

@app.route('/')
def index():
	return render_template('index.html')

app.run(debug=True)
