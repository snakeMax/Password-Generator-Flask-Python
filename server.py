from flask import Flask, render_template
import random, string
from flask_mysqldb import MySQL

app = Flask(__name__)

########################################### Variables //

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '2it'

########################################### Variables //


########################################### DATABASE //
 
mysql = MySQL(app)


def randomize():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!!!!!___", k=11))

def check_connection(statement):
    cursor = mysql.connection.cursor()
    cursor.execute(statement)
    cursor.close()
    return '<p>Connected to database!</p>'

def execute_command_sql(statement):
    cursor = mysql.connection.cursor()
    cursor.execute(statement)
    result = cursor.fetchone()
    return result

def connect_to_base():
    try:
        return check_connection(''' SELECT 1 ''')
    except Exception as e:
        print("\nThe error:\n" + str(e) + "\n")
        return '<p>Sql error!</p>'

########################################### DATABASE //

########################################### PAGES //

@app.route('/')
def website():
    return render_template('index.html', debug = connect_to_base())

@app.route('/login')
def login_page():
    return render_template('index.html', additional = '<p>Login page</p>')

@app.route('/data')
def data_page():
    return render_template('index.html', data = execute_command_sql("""SELECT * FROM elever WHERE 1""")[1])

########################################### PAGES //

if __name__ == '__main__':
   app.run(host='localhost', port=5000)
