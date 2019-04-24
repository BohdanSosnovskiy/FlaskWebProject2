from flask import Flask, render_template, request
from tasks import add

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        result = add.apply_async(args=[request.form['Text1'], request.form['Text2']])
        return render_template('index.html', id_task=result.id)
    else:
        return render_template('index.html')

@app.route('/result')
def result_task():
    return str(add.AsyncResult(str(request.headers.get('result_id'))))

if __name__ == '__main__':
    app.run()
