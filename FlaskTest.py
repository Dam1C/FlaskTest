from flask import Flask, render_template, json, request
#from flask.ext.pymongo import PyMongo
from querys import *
from pymongo import MongoClient
import hashlib

app = Flask(__name__)


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
        return showSignUp()
    #if _name and _email and _password:
     #   return json.dumps({'html':'<span>All fields good !!</span>'})
    #else:
    #    return json.dumps({'html':'<span>Enter the required fields</span>'})


if __name__ == '__main__':
    app.run()
