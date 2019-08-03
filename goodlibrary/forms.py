from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectMultipleField, SubmitField
from wtforms.validators import InputRequired


class ListSearchForm(FlaskForm):
    file = FileField(
        'Step 2: Upload your Goodreads list csv file', 
        [FileRequired('Please upload the list'), FileAllowed(['csv'], 'That appears to be the wrong file')])
    libraries = SelectMultipleField(
        'Step 3: Choose libraries to search (select multiple by holding Ctrl)', 
        [InputRequired('Please select at least 1 library')],
        choices=[
            ('perth', 'Australia/WA/Perth/City of Perth Library')])
    submit = SubmitField('Search')

