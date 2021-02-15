from flask import (
	Blueprint,
	render_template,
	request,
	redirect,
	url_for,
)
from flask_login import(
	login_required
)
from .view import InfoForm

bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@bp.route('/', methods=['GET'])
@login_required
def index():
	return render_template('home.html')

@bp.route('/modify_info')
def modify_info():
	info_form = InfoForm()
	return render_template('modify_info.html', form=info_form)

@bp.route('/submit_info', methods=['POST'])
def submit_info():
	info_form = InfoForm()
	return redirect(url_for('home.index'))


