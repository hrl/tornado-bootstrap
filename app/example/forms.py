from form import Form

from wtforms.fields import IntegerField


class ExampleForm(Form):
    n = IntegerField('n')
