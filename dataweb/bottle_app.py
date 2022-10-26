
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template
import sqlite3

connection = sqlite3.connect("shopping_list.db")

@route('/hi')
def hi_world():
    return 'Hi from Sundeep!'

@route('/hello')
def hello_world():
    return 'Hello from Sundeep!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return template("shopping_list.tpl", name = "Ganesh", shopping_list=rows)

application = default_app()

