

# -*- coding:utf8 -*-
from flask import Flask, render_template
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template('flask_template.html', page = "Home Page")

# Hello Page
@app.route("/hello/")
def hello():
    return render_template('flask_template.html', page = "Welcome page")
# Posts Page
@app.route("/posts")
def posts():
    posts = [
    "The content of the first article",
    "The content of the second article",
    "The content of the third article",
    "The content of the fourth article"
    ]

    return render_template('flask_posts.html', posts = posts, page = "Article Display Page")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
