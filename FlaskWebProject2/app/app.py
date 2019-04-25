"""Include moduls"""
from flask import Flask

from flask import render_template
from flask import request
from tasks import add

APP = Flask(__name__)

WSGI_APP = APP.wsgi_app


@APP.route('/')
def index():
    """This is home page"""
    return render_template('home_page.html')


@APP.route('/new', methods=['GET', 'POST'])
def new_task():
    """Page added new Tasks"""
    if request.method == 'POST':
        result = add.apply_async(args=[request.form['Text1'], request.form['Text2']])
        return render_template('index.html', id_task=result.id)

    return render_template('index.html')


@APP.route('/result')
def result_task():
    """Page all resukt by id task"""
    return str(add.AsyncResult(str(request.headers.get('result_id'))))

if __name__ == '__main__':
    APP.run()
