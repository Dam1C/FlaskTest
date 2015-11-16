
from pymongo import MongoClient



def citiesQuery(mongoquery):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ


    cursor = db.cities.find({"name":mongoquery})

    return cursor;

def sesionQuery(mail):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"mail":mail.lower})

    return cursor;


def loginQuery(mail,hashPass):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"mail":mail.lower()})

    for u in cursor:
        if u.get("password") == hashPass:
            return True

    return False;

def registerQuery(user,mail,hashPass):

    client = MongoClient()

    client = MongoClient("mongodb://10.1.133.102:27017")

    db = client.examenLOCALIZ

    cursor = db.users.find({"user":user.lower()})

    for c in cursor:
        return False;

    result = db.users.insert(
            {
                "user":user.lower(),
                "password":hashPass,
                "mail":mail.lower()
            })
    return True;


