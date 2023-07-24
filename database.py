import os
from datetime import date
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
HOST = os.environ['HOST_MONGODB']
PORT = os.environ['PORT_MONGODB']
DB = os.environ['DB_MONGODB']

client = MongoClient(host=HOST, port=int(PORT))
# db = client.subscan
db = client[DB]
filesC = db.files  # Collection: files
urlsC = db.urls  # Collection: urls


def close_db():
    client.close()


def mod_url(url):
    # --Modify for find any url in the data base
    if "https://" in url:
        return url.replace("https://", "")
    elif "http://" in url:
        return url.replace("http://", "")
    else:
        return url


def checkFile(hash, hash_alg, engine):
    try:
        res = filesC.find_one({"engine": engine, f'payload.{hash_alg}': {
                              '$regex': f'^{hash}$', '$options': 'i'}})
        if res != None:
            return res['payload']
        return None
    except Exception:
        return None


def insertFileData(data, engine):
    create_date = str(date.today())
    try:
        res = filesC.insert_one({'created_date': create_date,
                                 "modified_date": "",
                                 "engine": engine, "payload": data})
        return {"status": "ok", 'id': res.inserted_id, "msg": "Valor Insertado con Exito"}
    except Exception:
        return {"status": "error", "msg": "No se pudo Insertar Valores"}

def updateFileData(hash, hash_alg, engine, new_data):    
    query_filter = {"engine": engine, f'payload.{hash_alg}': {'$regex': f'^{hash}$', '$options': 'i'}}
    now_date = str(date.today())
    try:     
        query = filesC.find_one(query_filter)
        past_date = query['created_date']
    except Exception:
        return {"status": "error", "msg": "No se pudo Actualizar Valores"}
    try:
        if past_date != now_date:
            new_values = {'$set': {"created_date": past_date, "modified_date": now_date,
                                  "engine": engine, "payload": new_data}}
            filesC.update_one(query_filter, new_values)                        
            return {"status": "ok", "msg": "Valores Actualizados con Exito"}
        return {"status": "ok", "msg": "Los Valores se Encuentran Actualizados"}
    except Exception:
        return {"status": "error", "msg": "No se pudo Actualizar Valores"}

def deleteAllFileData():    
    try:
        if filesC.count_documents({}) > 0:
            filesC.delete_many({})
            return {"status": "ok", "msg": "Se Eliminaron todos los Registros de los Files"}
        return {"status": "error", "msg": "La base de datos esta vacia"}
    except Exception:
        return {"status": "error", "msg": "No se pudo Eliminar los Registros de los Files"}

def checkUrl(url, engine):
    url_mod = mod_url(url)
    try:
        res = urlsC.find_one(
            {'engine': engine, 'payload.url': {'$regex': f'.*{url_mod}.*', '$options': 'i'}})
        if res != None:
            return res['payload']
        return None
    except Exception:
        return None


def insertUrlData(data, engine):
    create_date = str(date.today())
    try:
        res = urlsC.insert_one({"created_date": create_date,
                                "modified_date": "",
                                "engine": engine, "payload": data})
        return {"status": "ok", 'id': res.inserted_id, "msg": "Valor Insertado con Exito"}
    except Exception:
        return {"status": "error", "msg": "No se pudo Insertar Valores"}


def updateUrlData(url, engine, new_data):
    url_mod = mod_url(url)
    query_filter = {'engine': engine, 'payload.url': {'$regex': f'.*{url_mod}.*', '$options': 'i'}}
    now_date = str(date.today())
    try:     
        query = urlsC.find_one(query_filter)
        past_date = query['created_date']
    except Exception:
        return {"status": "error", "msg": "No se pudo Actualizar Valores"}
    try:
        if past_date != now_date:
            new_values = {'$set': {"created_date": past_date, "modified_date": now_date,
                                  "engine": engine, "payload": new_data}}
            urlsC.update_one(query_filter, new_values)                        
            return {"status": "ok", "msg": "Valores Actualizados con Exito"}
        return {"status": "ok", "msg": "Los Valores se Encuentran Actualizados"}
    except Exception:
        return {"status": "error", "msg": "No se pudo Actualizar Valores"}

def deleteAllUrlsData():
    try:
        if urlsC.count_documents({}) > 0:
            urlsC.delete_many({})
            return {"status": "ok", "msg": "Se Eliminaron todos los Registros de las URLS"}
        return {"status": "error", "msg": "La base de datos esta vacia"}
    except Exception:
        return {"status": "error", "msg": "No se pudo Eliminar los Registros de las URLS"}