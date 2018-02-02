# -*- coding:utf8 -*-
from flask import Flask, render_template
app = Flask(__name__)

# Posts Page
@app.route("/posts")
def posts():
    posts = [
    u"مُحتوى المقال الأول",
    u"مُحتوى المقال الثاني",
    u"مُحتوى المقال الثالث",
    u"مُحتوى المقال الرابع"
    ]
    return render_template('flask_posts.html', posts = posts, page = u"صفحة عرض المقالات")
