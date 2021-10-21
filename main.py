from flask import Flask, request, render_template
from werkzeug.utils import redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def validate():
    username= request.form['username']
    password= request.form['password']
    confirm= request.form['confirm_password']
    email= request.form['email']
    user_error = ''
    pass_error = ''
    con_error = ''
    mail_error = ''

    if username =='':
        user_error = 'Input required'
    
    if password =='':
        pass_error = 'Input required'
    
    if confirm =='':
        con_error = 'Input required'
    
    if username.__contains__(" "):
        user_error = 'Username cannont contain a space'
    
    if len(username) < 3 or len(username) > 20:
        user_error = 'Username is not 3-20 characters long'
    
    if len(password) < 3 or len(password) > 20:
        pass_error = 'Password is not 3-20 characters long'
    
    if password != confirm:
        con_error = "Passwords do not match"

    if email != '':
        if "@" not in email or "." not in email or email.__contains__(" ") or len(email) < 3 or len(email) > 30:
            mail_error= "Please enter a valid email"    

    if not user_error and not pass_error and not con_error and not mail_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username_error=user_error ,password_error=pass_error,confirm_error=con_error, email_error=mail_error, username=username, email=email )

@app.route('/welcome')
def welcome():
    user = request.args.get('username')
    return render_template('welcome.html', username=user)


    

    
app.run()