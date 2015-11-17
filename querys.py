
from pymongo import MongoClient



def coordenadesCiutat(mongoquery,codPais):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ


    cursor = db.cities.find({"name":mongoquery})

    print(cursor.count())

    if cursor.count() != 0:
        for u in cursor:
            if u.get("country") == codPais:
                loc = u.get("loc")
    else:
        loc = None


    return loc;






def loginQuery(mail,hashPass):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"mail":mail.lower()})

    for u in cursor:
        if u.get("password") == hashPass:
            user = u.get("user")
            return user

    return None;

def registerQuery(user,mail,hashPass):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

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
                "mail":mail.lower()
            })
    return True;


