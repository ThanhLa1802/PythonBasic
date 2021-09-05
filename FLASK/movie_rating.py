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

from mysql.connector import connect, Error
app  = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=2)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

def create_connection():
    select_movies_query = """
     SELECT CONCAT(title, " (", release_year, ")"),
           collection_in_mil
     FROM movies
     ORDER BY collection_in_mil DESC
     LIMIT 5
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
                # for db in cursor:
                #     print(db)
                # cursor.execute(create_movies_table_query)
                # cursor.execute(create_reviewers_table_query)
                # cursor.execute(create_ratings_table_query)
                # connection.commit()
                # cursor.executemany(insert_ratings_query, ratings_records)
                cursor.execute(select_movies_query)
                # Fetch rows from last executed query
                result = cursor.fetchall()
                return result
    except Error as e:
        print(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/view")
def view():
    return render_template("view.html", values = create_connection() )
if __name__ == "__main__":
    app.run(debug=True)