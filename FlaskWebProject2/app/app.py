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



@app.route('/new', methods=['GET', 'POST'])
def new_task():
    #result = add.apply_async(arg = [10, 20])
    try:

        result = add.delay(4,4)
    except Exception as e:
        print(str(e))
    try:
        print(result.ready())
    except:
        print('error: ready')
    try:
        print(result.wait())
    except:
        print('error: wait')

    print('=================================')
    try:
        print(result.get())
    except:
        print('error: get')
    
    return 'Welcome to my app!'

@app.route('/result/<id_result>')
def send_image(id_result):
    return id_result.ready()

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '6379'))
    except ValueError:
        PORT = 6379
    app.run()
