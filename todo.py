__author__ = 'rbastian'

import sqlite3
import bottle

@bottle.route('/todo')
def todo_list():
    """

    """
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    output = bottle.template('make_table', rows=result)
    return output

@bottle.route('/new', method='GET')
def new_item():

    """

    """

    if bottle.request.GET.get('save','').strip():

        new = bottle.request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return bottle.template('new_task.tpl')

bottle.run()
