# app.py - Main starting point of application

from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

#app global
app = Flask(__name__)

#creating app secret to enable me use sessions later
app.secret_key = 'aaUDndid8395r-%98374+nsunbs'

#in order to prevent ambiguity for this simple proof-of-concept ptoject I will use 
# a python dictionaly as my global database

#format of entries: username: {password_hash, user posts}
registerdUsers = {
    'george':{
        'password_hash': generate_password_hash("hello1234"),
        'posts':[
            {'content':'This is my first post!', 'author':'George'},
            {'content':'This is my second post!', 'author':'George'},
        ]
    },
    'sam':{
        'password_hash': generate_password_hash('hello1234'),
        'posts':[
            {'content':'This is my first post!', 'author':'Sam'},
            {'content':'This is my second post!', 'author':'Sam'},
        ]
    }
}

#Below are the route definitions and view functions


#home route and view functions
@app.route('/')
@app.route('/home')
def home():
    if 'username' not in session: #simply check if user has been logged in
        #redirect user to login page to login
        return redirect(url_for('login'))

    #if the user is logged in fecth all  posts
    allPosts = []
    for userData in registerdUsers.values():
        allPosts.extend(userData['posts'])
    #render the home template
    return render_template("home.html", username=session['username'], posts=allPosts)


#LOGIN route and view functions
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST": #handling a submitted form to the endpoint
        username = request.form['username']
        password = request.form['password']

        #checking existenece of credentials in database, then login else throw error
        if username in registerdUsers:
            #validating password
            if check_password_hash(registerdUsers[username]['password_hash'], password):
                #if credentials are vlid, login and store the username in session
                session["username"] = username
                #redirecting to the homepage
                return redirect(url_for('home'))
            else:
                #raise error since user password was wrong
                error = 'Invalid password'
                return render_template('login.html', error=error)
        #if the username is not in the database
        else:
            error = 'Invalid username'
            return render_template('login.html', error=error)
    #to handle other requests(Specifically get request)
    return render_template('login.html')


#profile route and view functions
@app.route('/profile/<username>')
def profile(username):
    if 'username' not in session:
        return redirect(url_for('login')) #if the user is not logged in

    #check if the profile is in database
    if username in registerdUsers:
        userProfile = registerdUsers[username]
        #return the profile page with the user's data
        return render_template('profile.html', user_profile=userProfile, username=username)
    else:
        #if the profile does not exists, since no signup screen, redirect to the homepage
        return redirect(url_for('home'))


#logout route and view function
@app.route('/logout')
def logout():
    #remove the user's username from the session
    session.pop('username', None)
    #redirect to the login page
    return redirect(url_for('login'))

#main application start point
if __name__ == '__main__':
    app.run(debug=True)