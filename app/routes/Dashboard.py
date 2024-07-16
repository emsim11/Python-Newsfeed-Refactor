from flask import Blueprint, render_template

Blueprints = Blueprint('Dashboard', __name__, url_prefix='/dashboard')

@Blueprints.route('/')
def Dashboard():
    return render_template('Dashboard.html')

@Blueprints.route('/edit/<Id>')
def Edit(Id):
    return render_template('Edit-Post.html')