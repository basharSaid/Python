

# -*- coding:utf8 -*-
from flask import Flask, render_template
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template('flask_template.html', page = u"الصّفحة الرّئيسيّة")

# Hello Page
@app.route("/hello/")
def hello():
    return render_template('flask_template.html', page = u"صفحة التّرحيب")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
