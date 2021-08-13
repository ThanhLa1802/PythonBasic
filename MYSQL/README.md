### This sample is basic of MySQL wwith python follow realpython
# 1. Installing MySQL Server and MySQL Connector/Python
Now, to start working through this tutorial, you need to set up two things: a MySQL server and a MySQL connector. MySQL server will provide all the services required for handling your database. Once the server is up and running, you can connect your Python application with it using MySQL Connector/Python.

Installing MySQL Server
The official documentation details the recommended way to download and install MySQL server. For Windows, the best way is to download MySQL Installer and let it take care of the entire process: https://dev.mysql.com/downloads/installer/

Note: Remember the hostname, username, and password as these will be required to establish a connection with the MySQL server later on.

***Installing MySQL Connector/Python***

pip install mysql-connector-python

# 2. Establishing a Connection With MySQL Server
MySQL is a server-based database management system. One server might contain multiple databases. To interact with a database, you must first establish a connection with the server. The general workflow of a Python program that interacts with a MySQL-based database is as follows:

 - Connect to the MySQL server.
 - Create a new database.
 - Connect to the newly created or an existing database.
 - Execute a SQL query and fetch results.
 - Inform the database if any changes are made to a table.
 - Close the connection to the MySQL server.
