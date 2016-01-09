from flask import render_template, request, session, redirect, jsonify
# from flask.ext.pymongo import PyMongo
from querys import *
from flask import Flask, Markup
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from gmaps import Geocoding
import geocoder

app = Flask(__name__)
app.secret_key = 'GregorioSecretKey'
GoogleMaps(app)
mapsAPI = Geocoding()


@app.route('/')
def main():
    getCountries()
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # Coje los datos de nuestro formulario
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _lat = request.form['lat']
    _lon = request.form['lon']

    loc = {'latitude': _lat, 'longitude': _lon}

    # Insertamos
    result = registerQuery(_name, _email, _password, loc)
    if result != False:
        return "1"
    else:
        return "0"


@app.route('/showSignIn')
def showSignin():
    return render_template('signin.html')


@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    _username = request.form['inputEmail']
    _password = request.form['inputPassword']
    result = loginQuery(_username, _password)

    if result != None:
        # session['dict'] = result
        session['name'] = result.get('user')
        session['mail'] = result.get('mail')
        session['loc'] = result.get('loc')
        return redirect('/userHome')
    else:
        return render_template('error.html', error='El email o password no es correcto.')


@app.route('/userHome')
def userHome():
    if session:
        # loc = coordenadesCiutat("Barcelona","ES")
        loc = getCoordCasa(session.get('mail'))
        if loc.get('latitude') != "" and loc.get('longitude') != "":
            latMongo = loc.get("latitude")
            lonMongo = loc.get("longitude")
        else:
            latMongo = 0  # TODO Cambiar mierda
            lonMongo = 0
        # Creamos mapas
        sndmap = Map(
            identifier="sndmap",
            lat=latMongo,
            lng=lonMongo,
            markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png': [(latMongo, lonMongo)]}  # ,
            # 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(37.4300, -122.1400)]}
        )
        return render_template('userHome.html', message='Bienvenido, ' + session.get('name').capitalize(),
                               sndmap=sndmap)  # Mostramos el nombre del usuario que inicia sesion. Capitalize es para que la primera letra sea mayuscula
    else:
        return render_template('error.html', error='Unauthorized Access')


@app.route('/ciutats')
def ciutats():
    lista = getCountries()
    paisosHTML = ""
    for pais in lista:
        paisosHTML += "<option>" + pais + "</option>\n"#<li><a href=""#"">" + pais + "</a></li>\n"

    paisosHTML = Markup(paisosHTML)
    return render_template('ciutats.html',paisos=paisosHTML)


@app.route('/logout')
def logout():
    # session.pop('dict',None)
    session.clear()
    return redirect('/')


@app.route("/map")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png': [(37.4419, -122.1419)],
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png': [(37.4300, -122.1400)]}
    )
    return render_template('example.html', mymap=mymap, sndmap=sndmap)

@app.route('/cercaCiutats', methods=['POST'])
def cercaCiutats():
    _paisos = request.form.getlist('paisosSelect')
    _paisos = [x.encode('utf-8') for x in _paisos]


    _poblacioMinim = request.form['poblacioMinim'].encode('utf-8')
    _poblacioMaxim = request.form['poblacioMaxim'].encode('utf-8')


    try:
        _poblacioMaxim = int(_poblacioMaxim)
    except ValueError:
       _poblacioMaxim = 999999999999

    try:
        _poblacioMinim = int(_poblacioMinim)
    except ValueError:
       _poblacioMinim = 0




    cursor = getCities(_paisos,_poblacioMinim,_poblacioMaxim)

    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png': [(37.4419, -122.1419)],
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png': [(37.4300, -122.1400)]}
    )
    #i = 0
    #ciutats = ""
    #for c in cursor:
        #ciutats += "<h1>"+str(i)+":  "+c.get("name")+"</h1>"
       # i+=1
    return render_template('resultat.html', resul=cursor, sndmap = sndmap)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
