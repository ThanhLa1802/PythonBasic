# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:15:59 2021

@author: thanh 
follow: RealPython
"""
from mysql.connector import connect, Error

create_db_query = "CREATE DATABASE online_movie_rating"
show_db_query = "SHOW DATABASES"

create_movies_table_query = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""

create_reviewers_table_query = """
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""

create_ratings_table_query = """
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""

show_table_query = "DESCRIBE movies"

#change value
alter_table_query = """
     ALTER TABLE movies
     MODIFY COLUMN collection_in_mil DECIMAL(4,1)
     """
     
#delete table
drop_table_query = "DROP TABLE movies"

#insert value into table movies
insert_movies_query = """
INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Good Will Hunting", 1997, "Drama", 138.1),
    ("Skyfall", 2012, "Action", 304.6),
    ("Gladiator", 2000, "Action", 188.7),
    ("Black", 2005, "Drama", 3.0),
    ("Titanic", 1997, "Romance", 659.2),
    ("The Shawshank Redemption", 1994, "Drama",28.4),
    ("Udaan", 2010, "Drama", 1.5),
    ("Home Alone", 1990, "Comedy", 286.9),
    ("Casablanca", 1942, "Romance", 1.0),
    ("Avengers: Endgame", 2019, "Action", 858.8),
    ("Night of the Living Dead", 1968, "Horror", 2.5),
    ("The Godfather", 1972, "Crime", 135.6),
    ("Haider", 2014, "Action", 4.2),
    ("Inception", 2010, "Adventure", 293.7),
    ("Evil", 2003, "Horror", 1.3),
    ("Toy Story 4", 2019, "Animation", 434.9),
    ("Air Force One", 1997, "Drama", 138.1),
    ("The Dark Knight", 2008, "Action",535.4),
    ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
    ("The Lion King", 1994, "Animation", 423.6),
    ("Pulp Fiction", 1994, "Crime", 108.8),
    ("Kai Po Che", 2013, "Sport", 6.0),
    ("Beasts of No Nation", 2015, "War", 1.4),
    ("Andadhun", 2018, "Thriller", 2.9),
    ("The Silence of the Lambs", 1991, "Crime", 68.2),
    ("Deadpool", 2016, "Action", 363.6),
    ("Drishyam", 2015, "Mystery", 3.0)
"""
insert_reviewers_query = """
INSERT INTO reviewers
(first_name, last_name)
VALUES ( %s, %s )
"""
reviewers_records = [
    ("Chaitanya", "Baweja"),
    ("Mary", "Cooper"),
    ("John", "Wayne"),
    ("Thomas", "Stoneman"),
    ("Penny", "Hofstadter"),
    ("Mitchell", "Marsh"),
    ("Wyatt", "Skaggs"),
    ("Andre", "Veiga"),
    ("Sheldon", "Cooper"),
    ("Kimbra", "Masters"),
    ("Kat", "Dennings"),
    ("Bruce", "Wayne"),
    ("Domingo", "Cortes"),
    ("Rajesh", "Koothrappali"),
    ("Ben", "Glocker"),
    ("Mahinder", "Dhoni"),
    ("Akbar", "Khan"),
    ("Howard", "Wolowitz"),
    ("Pinkie", "Petit"),
    ("Gurkaran", "Singh"),
    ("Amy", "Farah Fowler"),
    ("Marlon", "Crafford"),
]
insert_ratings_query = """
INSERT INTO ratings
(rating, movie_id, reviewer_id)
VALUES ( %s, %s, %s)
"""
ratings_records = [
    (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14), (5.1, 21, 17),
    (5.0, 5, 5), (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4),
    (8.5, 24, 12), (9.9, 14, 9), (8.7, 26, 14), (9.9, 6, 10),
    (5.1, 30, 6), (5.4, 18, 16), (6.2, 6, 20), (7.3, 21, 19),
    (8.1, 17, 18), (5.0, 7, 2), (9.8, 23, 3), (8.0, 22, 9),
    (8.5, 11, 13), (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19),
    (5.2, 18, 15), (9.7, 13, 3), (5.8, 18, 8), (5.8, 30, 15),
    (8.4, 21, 18), (6.2, 23, 16), (7.0, 10, 18), (9.5, 30, 20),
    (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22), (9.9, 15, 13),
    (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17),
    (6.4, 5, 10), (8.1, 5, 21), (5.7, 22, 1), (6.3, 28, 4),
    (9.8, 13, 1)
]
#Reading Records Using the SELECT Statement
#select_movies_query = "SELECT * FROM movies LIMIT 5"

#Filtering Results Using the WHERE Clause

# select_movies_query = """
#      SELECT title, collection_in_mil
#      FROM movies
#      WHERE collection_in_mil > 300
#      ORDER BY collection_in_mil DESC
#      """

#CONCAT for concatenating strings.
select_movies_query = """
     SELECT CONCAT(title, " (", release_year, ")"),
           collection_in_mil
     FROM movies
     ORDER BY collection_in_mil DESC
     LIMIT 5
     """

#Handling Multiple Tables Using the JOIN Statement
#name of the top five highest-rated movies 
select_movies_query1 = """
    SELECT title, AVG(rating) as average_rating
    FROM ratings
    INNER JOIN movies
        ON movies.id = ratings.movie_id
    GROUP BY movie_id
    ORDER BY average_rating DESC
    LIMIT 5
    """
#find the name of the reviewer who gave the most ratings
select_movies_query2 = """
     SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
     FROM reviewers
     INNER JOIN ratings
        ON reviewers.id = ratings.reviewer_id
     GROUP BY reviewer_id
     ORDER BY num DESC
     LIMIT 1
     """
#Updating and Deleting Records From the Database
update_query = """
    UPDATE
        reviewers
    SET
        last_name = "Cooper"
    WHERE
        first_name = "Amy"
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
            # cursor.execute(show_db_query)
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
            for row in result:
                 print(row)
except Error as e:
    print(e)
