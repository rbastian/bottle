__author__ = 'rbastian'

import sqlite3
import bottle

@bottle.route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    output = bottle.template('make_table', rows=result)
    return output

bottle.run()
