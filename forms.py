from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(2, 20)])
    email = StringField('email', validators=[DataRequired(), Length(3, 30)])
    submit = SubmitField()

