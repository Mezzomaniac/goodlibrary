from flask import redirect, render_template, url_for#, flash, g, request, session

from goodlibrary import app
from goodlibrary.forms import ListSearchForm
from goodlibrary.processing import search


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ListSearchForm()
    if form.validate_on_submit():
        return 'file upload test ok'
        file = form.file.data
        libraries = form.libraries.data
        results = search(file, libraries)
        return render_template('results.html', title='Search results')
    return render_template('home.html', title='Home', form=form)

@app.route('/test')
def test():
    return redirect(url_for('home'))
    
