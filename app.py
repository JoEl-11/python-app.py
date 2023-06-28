from flask import Flask,render_template,request 
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tinytreasures"
)
mycursor = mydb.cursor()


app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template("/welcome.html")


@app.route('/signin')
def signin():
    return render_template("/signin.html")

@app.route('/signup')
def signup():
    return render_template("/signup.html")
@app.route('/submit-form', methods=['post'])
def submit_form():
    name = request.form['name']
    gender=request.form['gender']
    email = request.form['email']
    username=request.form['username']
    password1=request.form['password1']
    password2=request.form['password2']
    if(password1==password2):
        query="INSERT INTO signup (name,gender,email,username,password) VALUES (%s,%s,%s,%s,%s)"
        data=(name,gender,email,username,password2)
        mycursor.execute(query,data)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return render_template('home.html')
    else:
        return render_template('signup.html',msg="both password are different try again")
    
@app.route('/submit-login', methods=['GET'])
def login():
    email= request.args.get('email')
    password=request.args.get('pass')
    query=("SELECT password FROM signup WHERE email = %s")
    val=[email]
    mycursor.execute(query,val)
    check=mycursor.fetchone()
    if check is not None:
        stored_password = check[0]
        if password == stored_password:
            return render_template('home.html')
        else:
            return render_template('signin.html',msg="invalid password or username")


@app.route('/forgot password')
def forgotpass():
    
    return render_template("/forgot password.html")


if("__main__"==__name__):
    app.run(debug=True)