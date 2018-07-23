from main import app
# from .utils import *
from main.utils import *
from flask import abort, redirect, url_for
from flask import render_template
from main.common.errorcode import *


@app.route('/route1')
def r1():
    return "for test11111 "


@app.route('/notfound')
def notfound():
    abort(404)


@app.route('/error')
def error5():
    abort(500)


@app.route('/table')
def table(name=None):
    form = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
    return render_template('tabledata.html', data=form)


@app.route('/tablelist')
def tablelist(name=None):
    form = [['key1', '1111'], ['key12', '22222'], ['key123', '333333']]
    return render_template('tablelist.html', data=form)


@app.route('/home')
def temp1(name=None):
    return render_template('homepage.html', name=name)


# Post: http://127.0.0.1:5000/fetch/params    set param to body
# Get:  http://127.0.0.1:5000/fetch/params?un=liuhaiyang&pw=123456
@app.route('/fetch/params', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        printParam(request.form['un'], request.form['pw'])
        return "post method"
    else:
        print('get un=', request.args.get('un', 'defaultValue'))
        print('get pw=', request.args.get('pw', 'defaultValue'))
        return "get method"
