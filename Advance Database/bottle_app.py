from bottle import default_app, route, template, redirect
import sqlite3

connection = sqlite3.connect("shopping_list.db")
#import database

@route('/')
def get_index():
    redirect('/list')

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows=cursor.execute("select id,description from list")
    rows=list(rows)
    rows=[{'id':row[0],'desc':row[1]} for row in rows]

    return template("shopping_list.tpl", name="Sundeep", shopping_list=rows)





application = default_app()