
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

    cursor = db.users.find({"user":user.lower()})

    for c in cursor:
        return False;

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


