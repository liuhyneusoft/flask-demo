from flask import request
from flask import render_template
from main import app


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    app.logger.debug('/hello receive param name=', name)
    return render_template('hello.html', name=name)
