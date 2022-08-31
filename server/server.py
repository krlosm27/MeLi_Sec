from flask import Flask, request, jsonify
import json
import pymongo
from bson import json_util
import datetime

MONGODB_CONNECTION_STRING='mongodb://root:example@mongo:27017/'
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
    json_data = json.loads(json_util.dumps(payload))
    json_data['createdAt'] = datetime.datetime.utcnow()
    try:
        register = collection.insert_one(json_data)
        return jsonify(status_code=200, message="Succesfully registered")
    except Exception as e:
        print("An exception occurred ::", e)
        return jsonify(status_code=500, message="An exception ocurred = {e}")

@app.route("/servers/getMonitoring", methods=['GET'] )
def get_monitoring():
    listn =[]
    try:
        retrieves = collection.find().limit(10)
    except Exception as e:
        print("An exception occurred ::", e)
        return jsonify(status_code=500, message="Failed obtaining data from database")
        
    for document in retrieves:
        document = json_util.dumps(document)
        listn.append(json.loads(document))
    return jsonify(listn)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')