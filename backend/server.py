import os
from flask import Flask
from db_manager import DBManager


server = Flask(__name__)
conn = None

@server.route('/')
def listBlog():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response  + '<div>   Hello ' + c + '</div>'
    return response


if __name__ == '__main__':
    server.run()