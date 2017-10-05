
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/verify", methods = ['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error=''
    password_error=''
    email_error=''


    if username == '':
        username_error = "Username is required"
    elif len(username) <3 or len(username) >20:
        username_error = "Username must contain between 3 and 20 characters"
    elif ' ' in username:
        username_error = "Username may not contain spaces"

    if password == '':
        password_error = "Password is required"        
    elif len(password) <3 or len(password) >20:
        password_error = "Password must contain between 3 and 20 characters"
    elif ' ' in password:
        password_error = "Password may not contain spaces"
    elif verify_password != password:
        password_error = "Passwords must match"

    if len(email) != 0:
        if len(email) <3 or len(email) >20:
            email_error = "Email must contain between 3 and 20 characters"
        elif ' ' in email:
            email_error = "Email may not contain spaces"
        elif '@' not in email or '.' not in email:
            email_error = "Email address must contain  both '@' and '.' characters"
        
    if username_error == '' and password_error == '' and email_error == '':
        return render_template('welcome.html', username=username)
    
    else:
        return render_template('index.html',
        username=username,
        email=email,
        username_error=username_error,
        password_error=password_error,
        email_error=email_error)

@app.route("/")
def index():
    return render_template('index.html')

app.run()