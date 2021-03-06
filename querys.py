
from pymongo import MongoClient



def coordenadesCiutat(mongoquery,codPais):

    client = MongoClient()

    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.examenLOCALIZ


    cursor = db.cities.find({"name":mongoquery})


    if cursor.count() != 0:
        for u in cursor:
            if u.get("country") == codPais:
                loc = u.get("loc")
    else:
        loc = None


    return loc;

def getCoordCasa(mail):

    client = MongoClient()

    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"mail":mail.lower()})

    for c in cursor:
       return c.get("loc")



def loginQuery(mail,hashPass):

    client = MongoClient()

    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"mail":mail.lower()})

    for u in cursor:
        if u.get("password") == hashPass:
            return u

    return None;

def registerQuery(user,mail,hashPass,loc):

    client = MongoClient()

    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"mail":mail.lower()})

    for c in cursor:
        return False;

    result = db.users.insert(
            {
                "user":user.lower(),
                "password":hashPass,
                "mail":mail.lower(),
                "loc":loc
            })
    return True;


def getCountries():

    client = MongoClient()

    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.examenLOCALIZ

    pipeline =  [
                    { "$group" : { "_id" : "$country"} }
                ]

    cursor = db.cities.aggregate(pipeline)

    lista = []

    for c in cursor:
        lista.append(c.get("_id"))

    lista.sort()

    return lista

def getCities(paisos, poblacioMin, poblacioMax):

    client = MongoClient()

    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.examenLOCALIZ



    if poblacioMax <= 0 or poblacioMax == None:
        poblacioMax = 999999999999999

    if poblacioMin <= 0 or poblacioMin == None:
        poblacioMin = 0

    if paisos == None or paisos == []:
        cursor = db.cities.find({"population":{"$gte":poblacioMin,"$lte":poblacioMax}})#, "population":{"$lte":poblacioMax}})
    else:
        cursor = db.cities.find({"country": {"$in": paisos}, "population":{"$gte":poblacioMin,"$lte":poblacioMax}})#, "population":{"$lte":poblacioMax}})
    #cursor = db.cities.find({"country": {"$in": paisos}})


    data = cursor.count()


    return cursor
    #cursor = db.cities.find({"name":mongoquery})


    #if cursor.count() != 0:
    #    for u in cursor:
    #        if u.get("country") == codPais:
    #            loc = u.get("loc")
    ##else:
    #    loc = None


    #return loc;