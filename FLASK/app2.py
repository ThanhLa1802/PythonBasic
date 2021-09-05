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
from flask_sqlalchemy import SQLAlchemy
from mysql.connector import connect, Error
app  = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=2)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

def create_connection():
    select_movies_query2 = """
     SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
     FROM reviewers
     INNER JOIN ratings
        ON reviewers.id = ratings.reviewer_id
     GROUP BY reviewer_id
     ORDER BY num DESC
     LIMIT 1
     """
    try:
        with connect( #login into mysql
            host="localhost",
            # user=input("Enter username: "),
            # password=getpass("Enter password: "),
            user = 'thanhl1',
            password = 'abc13579',
            database = 'online_movie_rating', #init database
        ) as connection:
            with connection.cursor() as cursor:
                # cursor.execute(create_db_query)
                #cursor.execute(show_db_query)
                # for db in cursor:
                #     print(db)
                # cursor.execute(create_movies_table_query)
                # cursor.execute(create_reviewers_table_query)
                # cursor.execute(create_ratings_table_query)
                # connection.commit()
                # cursor.executemany(insert_ratings_query, ratings_records)
                cursor.execute(select_movies_query2)
                # Fetch rows from last executed query
                result = cursor.fetchall()
                return result
    except Error as e:
        print(e)
class users(db.Model):
    __tablename__ = 'users'
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def __init__(self, name, email):
        self.name = name
        self.email = email
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/view")
def view():
    return render_template("view.html", values = create_connection())
@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user_name = request.form["name"]
        session["user"] = user_name

        found_user = users.query.filter_by(name = user_name).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user_name, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template('login.html')
@app.route("/user", methods = ["POST", "GET"])
def user():
    email = None 
    if "user" in session:
        user_name = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name = user_name).first()
            found_user.email  = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template('user.html',email = email)
    else:
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("You have been logged out!", "infor")
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)