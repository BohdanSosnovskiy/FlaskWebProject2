from flask import Flask, render_template, request
from tasks import add

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def index():
    return 'Welcome to project'

list_result = []

@app.route('/new', methods=['GET','POST'])
def new_task():
    try:
       result = add.apply_async(args = [10, 20])
       list_result.append(result)
       url_for('result_task', id_result = id_result)
    except Exception as e:
       print(str(e))
            
    return result.id

@app.route('/result/<id_result>')
def result_task(id_result):
    return str(list_result[0].status)

if __name__ == '__main__':
    app.run()
