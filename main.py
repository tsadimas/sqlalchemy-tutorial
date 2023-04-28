from flask import Flask, render_template, redirect, request, flash, url_for
from models import User, Job
from config import SECRET_KEY

from database import db_session, init_db


app = Flask(__name__)
print(SECRET_KEY)
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


@app.route('/user', methods=['GET', 'POST'])
def newsuser():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['email']:
            flash('Please enter all the fields', 'error')
        else:
            user = User(
                username=request.form['username'], email=request.form['email'])
            db_session.add(user)
            db_session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new_user.html')



@app.route('/job/<uid>', methods=['POST'])
def savejob(uid):
    if not request.form['name']:
        flash('Please enter all the fields', 'error')
    else:
        user=User.query.get(uid)
        print(user)
        job = Job(name=request.form['name'], user=user)
        db_session.add(job)
        db_session.commit()
        flash('Record was successfully added')
    return redirect(url_for('show_all'))


@app.route('/job/<uid>', methods=['GET'])
def createjob(uid):
    user = db_session.get(User, uid)
    return render_template('new_job.html', user=user)
