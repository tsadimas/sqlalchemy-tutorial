from database import db_session, init_db
from flask import Flask, render_template
from models import User

app = Flask(__name__)

with app.app_context():
    init_db()



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()


@app.route('/')
def show_all():
    users = User.query.all()
    return render_template('show_all.html', users=users)
