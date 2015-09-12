import sqlite3
from bottle import route, run, debug, template, request

@route('/violations')
def violaitons():
	conn = sqlite3.connect('ghack5-1.db')
	c = conn.cursor()
	#c.execute("SELECT id, task FROM todo WHERE status LIKE '0'")
	#c.execute("SELECT id, violation_descriptions, citation_number FROM violations")
	c.execute("SELECT * FROM violations")
    #c.execute("SELECT id, citation_number FROM violations")
	result = c.fetchall()
	c.close()
	#print result
	output = template('make_table', rows=result)
	return output
    #return result

@route('/citations')
def citations():
    conn = sqlite3.connect('ghack5')
    c = conn.cursor()
    #c.execute("SELECT id, task FROM todo WHERE status LIKE '0'")
    #c.execute("SELECT id, citation_number FROM citations")
    c.execute("SELECT * FROM citations")
    #c.execute("SELECT id, citation_number FROM violations")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

# @route('/new', method='GET')
# def new_item():

#     if request.GET.get('save','').strip():

#         new = request.GET.get('task', '').strip()
#         conn = sqlite3.connect('todo.db')
#         c = conn.cursor()

#         c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
#         new_id = c.lastrowid

#         conn.commit()
#         c.close()

#         return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
#     else:
#         return template('new_task.tpl')

	
debug(True)
#run(reloader=True, host='10.4.245.19', port=8080)
run(reloader=True, port=8080)



con.execute("CREATE TABLE citations (id INTEGER PRIMARY KEY, citation_number INTEGER, first_name text, last_name text, date_of_birth datetime, defendant_address text, defendant_city text, defendant_state text, court_date text, court_location text, court_address text)")
con.execute("CREATE TABLE violations (id INTEGER PRIMARY KEY, citation_number INTEGER, violation_description text, warrant_status bool, warrant_number text, status text, fine_amount text, court_cost text)")