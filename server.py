from flask import Flask, render_template, request, redirect
import random, string
from flask_mysqldb import MySQL

app = Flask(__name__)

########################################### GLOBAL VARIABLES //

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '2it'

########################################### GLOBAL VARIABLES //


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

########################################### URL PROCESSING //

@app.route('/')
def website_main_page():
    return render_template('index.html', debug = connect_to_base())

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    language = request.args.get('language')
    return render_template('index.html', additional = 'Login page', data = 'language is {}'.format(language))

@app.route('/data', methods=['GET', 'POST'])
def data_page():
    if request.args.get('user') != None:
        usern = request.args.get('user')
        return render_template('index.html', data = execute_command_sql("""SELECT * FROM elever WHERE Fornavn='{}'""".format(usern), ''))

    return render_template('index.html', data = 'Database info')

@app.route('/edit', methods=['GET', 'POST'])
def edit_data_page():
    if request.args.get('user' and 'to') != None:
        usern = request.args.get('user')
        uid = execute_command_sql("""SELECT ID FROM elever WHERE Fornavn='{}'""".format(usern), '')
        to = request.args.get('to')
        return render_template('index.html', data = execute_command_sql("""UPDATE elever SET Fornavn='{}' WHERE ID='{}'""".format(to, uid), ''))
    
    return render_template('index.html', additional = 'Change Data')

########################################### URL PROCESSING //

if __name__ == '__main__':
   app.run(host='localhost', port=5000)
