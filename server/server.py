from flask import Flask, request
import json
import pymongo
from bson import json_util

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
    print(type(json_data))
    register = collection.insert_one(json_data)
    return payload

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')