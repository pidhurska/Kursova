import pymongo
conn = pymongo.Connection()
db = conn.mydb
coll = db.mycoll
doc = {"name":"Иван", "surname":"Иванов"}
coll.save(doc)
for men in coll.find({"name": "Петр"}):
    print (men["surname"])