from flask import Flask, render_template, json, request, session, redirect
#from flask.ext.pymongo import PyMongo
from querys import *
from pymongo import MongoClient
import hashlib


app = Flask(__name__)
app.secret_key = 'GregorioSecretKey'


@app.route('/')
def main():

    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():

    # Coje los datos de nuestro formulario
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']



    # Insertamos
    result = registerQuery(_name,_email,_password)
    if result:
        showSignin()
        return redirect('/')
    else:
        return render_template('error.html',error = 'El usuario ya existe.')


@app.route('/showSignIn')
def showSignin():
    return render_template('signin.html')

@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    _username = request.form['inputEmail']
    _password = request.form['inputPassword']
    result = loginQuery(_username,_password)
    data = sessionQuery(_username)




    if result:
        session['user'] = 1
        return redirect('/userHome')
    else:
        return render_template('error.html',error = 'Wrong Email address or Password.')

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html',message = 'BIENVENIDO GUARRA')
    else:
        return render_template('error.html',error = 'Unauthorized Access')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

if __name__ == '__main__':
    app.run()
