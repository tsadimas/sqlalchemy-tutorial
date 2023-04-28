from database import db_session, init_db
from flask import Flask, render_template, redirect
from models import User
from forms import UserForm
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

with app.app_context():
    init_db()



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()


@app.route('/')
def show_all():
    users = User.query.all()
    return render_template('show_all.html', users=users)

@app.route('/users', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    # if form.validate_on_submit():
    #     return redirect('/')
    return render_template('new_user.html', form=form)