from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'simple'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()




@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup',methods=['POST'])
def signupPost():
    print(request.form)
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    password = generate_password_hash(password)
    cursor.callproc('sp_createUser', (email, password))
    data = cursor.fetchall()
    print(1)
    if len(data) is 0:
        print(2)
        conn.commit()
        return json.dumps({'message': 'User created successfully !'})
    else:
        print(3)
    return json.dumps({'error': str(data[0])})

@app.route('/')
def index():
    cursor.callproc('getAllUsers')
    data = cursor.fetchall()
    return render_template('signup.html')

if (__name__ == "__main__"):
    app.run(host='0.0.0.0')



