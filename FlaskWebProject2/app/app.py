from flask import Flask, render_template
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@celery.task
def add(x, y):
    result = x * y
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders a sample page."""
    return render_template('index.html')



@app.route('/new', methods=['POST'])
def new_task():
    task = add.delay(4,4)
    return task

@app.route('/result/<id_result>')
def send_image(id_result):
    return id_result.ready()

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
