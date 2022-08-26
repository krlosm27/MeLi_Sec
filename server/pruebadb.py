import pymongo

dbConection = pymongo.MongoClient("mongodb://localhost:27017")## variable para la conexion
monitoringDb = dbConection["dbMeliSec"] #crear la base de datos
collection = monitoringDb["comandos"] #collection
comando = {"name":"carlos", "apellido":"buitrago"}
register = collection.insert_one(comando)
print (register)
