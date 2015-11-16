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
        return main()
    else:
        return main()


@app.route('/showSignIn')
def showSignin():
    return render_template('signin.html')

@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    _username = request.form['inputEmail']
    _password = request.form['inputPassword']
    result = loginQuery(_username,_password)
    dataMongo = sesionQuery(_username)

    

    for c in dataMongo:
        data[0][0] = c.get("_id")
    #data[0][0]= dataMongo.get("_id")
    #data[0][1]= dataMongo.get("user")
    #data[0][2]= dataMongo.get("mail")
    #data[0][3]= dataMongo.get("password")



    if result:
        #session['user'] = dataMongo.get("_id")
        return redirect('/userHome')
    else:
        return render_template('error.html',error = 'Wrong Email address or Password.')

@app.route('/userHome')
def userHome():
    return render_template('userHome.html')

if __name__ == '__main__':
    app.run()
