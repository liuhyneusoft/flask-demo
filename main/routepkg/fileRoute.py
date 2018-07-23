from main import app
# from .utils import *
from main.utils import *
from flask import abort, redirect, url_for
from flask import render_template
from main.common.errorcode import *
from flask import send_file, send_from_directory
import os

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        f.save('files/uploaded_file.txt')
    allfileset = []
    allfileset.append("files/ffff1111.txt")
    allfileset.append("files/ffff22222.txt")
    return render_template('homepage.html', allfileset=allfileset)


@app.route('/download', methods=['GET', 'POST'])
def download_file():
    print(os.getcwd())  #C:\Users\Naver\IdeaProjects\ppyy\flask3
    return send_from_directory(os.getcwd()+"/files", "uploaded_file.txt", as_attachment=True)


@app.route('/download/pic', methods=['GET', 'POST'])
def download_pic():
    return app.send_static_file("images/dd.PNG")
