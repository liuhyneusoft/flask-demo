from main import app
# from .utils import *
from main.utils import *

@app.route('/test1')
def test1():
    testUtil2();
    return "for test " + app.config['MAIN_URL'];

@app.route('/test2')
def test2():
    return redirect(app.config['MAIN_URL']);

