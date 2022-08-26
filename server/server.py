from flask import Flask, request
import json
import pymongo

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Prueba </p>"



dbConection = pymongo.MongoClient("mongodb://localhost:27017")## variable para la conexion
monitoringDb = dbConection["dbMeliSec"] #crear la base de datos
collection = monitoringDb["comandos"] #collection

@app.route("/servers/monitoring", methods=['POST'])
def servers_monitoring():
    payload = request.json
    dbConection = pymongo.MongoClient("mongodb://localhost:27017")
    register = collection.insert_one(payload)
    return payload

#dbConection = pymongo.MongoClient("mongodb://localhost:27017")## variable para la conexion
#monitoringDb = dbConection["dbMeliSec"] #crear la base de datos
#collection = monitoringDb["comandos"] #collection
##comando = {"name":"Alex", "apellido":"mijito"}
#register = collection.insert_one(payload)
##print (register)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')