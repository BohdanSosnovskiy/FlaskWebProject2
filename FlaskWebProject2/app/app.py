from flask import Flask, render_template, request
from celery import Celery
import traceback

app = Flask(__name__)


celery = Celery('tasks', broker="amqp://guest@localhost//", backend="amqp://")
celery.conf.update(app.config)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@celery.task
def add(x, y):
    result = x + y
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders a sample page."""
    return render_template('index.html')

list_result = []

@app.route('/new', methods=['GET','POST'])
def new_task():
    try:
       result = add.apply_async(args = [10, 20])
       list_result.append(result)
       print(list_result)
       url_for('result_task', id_result = id_result)
    except Exception as e:
       print(str(e))
            
    return result.id

@app.route('/result/<id_result>')
def result_task(id_result):
    try:
        obj = list_result[0]
        result = obj.status
    except Exception as e:
        result = str(e)
    return str(result)

if __name__ == '__main__':
    app.run()
