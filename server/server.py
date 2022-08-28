from flask import Flask, request, jsonify
import json
import pymongo
from bson import json_util
import datetime

MONGODB_CONNECTION_STRING='mongodb://localhost:27017/'
MONGODB_DATABASE_NAME='dbMeliSec'
MONGODB_COLLECTION='monitoring'

dbConection = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
meliSecDb = dbConection[MONGODB_DATABASE_NAME]
collection = meliSecDb[MONGODB_COLLECTION]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Prueba </p>"

@app.route("/servers/monitoring", methods=['POST'])
def servers_monitoring():
    payload = request.json
    print(type(payload))
    json_data = json.loads(json_util.dumps(payload)) 
    register = collection.insert_one(json_data)
    return(payload)

@app.route("/servers/getMonitoring", methods=['GET'] )
def get_monitoring():
    dictn = {}
    retrieves = collection.find().limit(10)
    for document in retrieves:
        dictn.update(document)
    jsonstring = json_util.dumps(dictn)
    print(type(jsonstring))
    return jsonify(jsonstring)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
    