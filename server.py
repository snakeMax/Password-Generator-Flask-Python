from flask import Flask, render_template
import random, string
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '2it'
 
mysql = MySQL(app)


def randomize():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!!!!!___", k=11))

def sql_command(statement):
    cursor = mysql.connection.cursor()
    cursor.execute(statement)
    cursor.close()
    return '<h1>Query success!</h1>'

def connect_to_base():
    try:
        return sql_command(''' SELECT 1 ''')
    except Exception as e:
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Sql error!</h1>'


@app.route('/')
def website():
    return render_template('index.html', r = randomize(), debug = connect_to_base())

if __name__ == '__main__':
   app.run(host='localhost', port=5000)