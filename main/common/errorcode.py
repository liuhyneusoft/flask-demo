from main import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('common/404.html'), 404


@app.errorhandler(500)
def error500(error):
    print(error)
    return render_template('common/500.html'), 500
