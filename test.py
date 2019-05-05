
import pymongo

sls = "mongodb+srv://Anastasia:20000103n!@cluster0-voyl5.mongodb.net/test?retryWrites=true&ssl_match_hostname=false&ssl_cert_reqs=CERT_NONE"
client = pymongo.MongoClient ( sls )
db = client.My_mogo
db2 = db.My_mogo

#doc = {"Login": "astia", "Password": "20000103","Name": "Anastasia","Surname": "Pidgu", "Facebook": "",}
#post_id = db2.insert_one (doc ).inserted_id

print(db2.find({"Login":"astia"}).count())