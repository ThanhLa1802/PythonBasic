# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:04:08 2021
@author: thanh
"""
from flask import Flask, render_template, request, flash
from flask.globals import session
from flask.helpers import url_for
from werkzeug.utils import redirect
from datetime import timedelta
app  = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=2)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user_name = request.form["name"]
        session["user"] = user_name
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('login.html')
@app.route("/user")
def user():
    if "user" in session:
        user_name = session["user"]
        return f"<h1>{user_name}</h1>"
    else:
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out!", "infor")
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)