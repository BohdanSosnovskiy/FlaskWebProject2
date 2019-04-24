from flask import Flask, render_template
from tasks import add

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def index():
    return render_template('index.html')

list_result = []

@app.route('/new', methods=['POST'])
def new_task():
    if request.method == 'POST':
        result = add.apply_async(args=[request.form['Text1'], request.form['Text2']])
        list_result.append(result)
        request.form['TextArea1'] = result.id
        return result.id

@app.route('/result/<id_result>')
def result_task(id_result):
    return str(list_result[0].status)

if __name__ == '__main__':
    app.run()
