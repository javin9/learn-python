from wtforms import Form, StringField  # noqa
from wtforms.validators import DataRequired, length

from app.forms.request_form import RequestForm


class UserForm(RequestForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password',
                           validators=[DataRequired(),
                                       length(min=6, max=20)])


class UserQuery(RequestForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password',
                           validators=[DataRequired(),
                                       length(min=6, max=20)])
