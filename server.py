from flask import Flask, render_template
import random, string
app = Flask(__name__)

def randomize():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!!!!!___", k=11))

@app.route('/')
def website():
    rstring = randomize()
    return render_template('index.html', r = rstring)

if __name__ == '__main__':
   app.run()