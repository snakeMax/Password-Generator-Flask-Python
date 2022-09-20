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
    return 'Connected to database!'

def execute_command_sql(statement, index):
    cursor = mysql.connection.cursor()
    cursor.execute(statement + index)
    result = cursor.fetchone()
    return result

def connect_to_base():
    try:
        return check_connection(''' SELECT 1 ''')
    except Exception as e:
        print("\nThe error:\n" + str(e) + "\n")
        return 'Sql error!'

########################################### DATABASE //

########################################### PAGES //

@app.route('/')
def website():
    return render_template('index.html', debug = connect_to_base())

@app.route('/login')
def login_page():
    return render_template('index.html', additional = 'Login page')

@app.route('/data')
def data_page():
    index = 1
    return render_template('index.html', data = execute_command_sql("""SELECT * FROM elever WHERE """, str(index)))

########################################### PAGES //

if __name__ == '__main__':
   app.run(host='localhost', port=5000)
