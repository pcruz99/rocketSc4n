from scripts import get_file_hash
from .engines.analizer_vt import get_file_report, get_url_report
from .engines.analizer_kp import looking_hash_file, looking_web_address
from database import (checkFile, insertFileData,
                      close_db, checkUrl, insertUrlData,
                      updateFileData, updateUrlData,
                      deleteAllFileData, deleteAllUrlsData)

# The engines could be VirusTotal like 'vt' and Kaspersky like 'kp'

# Verificar la base de datos local y comparar si el registro es actual o no para actualizarlo automaticamente
# def check_local_data(*args):
#     pass


def explore_file(path: str,
                 hash_alg: str = 'md5',
                 engine: str = 'vt',
                 update: bool = False
                 ):
    file_hash = get_file_hash(path, hash_alg)
    localData = checkFile(file_hash, hash_alg, engine)
    if localData != None and not update:
        close_db()
        return [localData, {"status": "ok", "msg": "Valores consultados en Base de Datos Local"}]

    match engine:
        case 'vt':
            data = get_file_report(file_hash)
        case 'kp':
            data = looking_hash_file(file_hash)
        case _:
            pass

    if data['status'] == 'ok' and not update:
        status = insertFileData(data['data'], engine)
    elif update:
        status = updateFileData(file_hash, hash_alg, engine, data['data'])

    close_db()
    if data['status'] == 'error':
        status = {'status': data['status'], 'msg': data['msg']}
    data = data['data']

    return [data, status]


def explore_url(url: str, engine: str = 'vt', update: bool = False):
    localData = checkUrl(url, engine)

    if localData != None and not update:
        close_db()
        return [localData, {"status": "ok", "msg": "Valores consultados en Base de Datos Local"}]

    match engine:
        case 'vt':
            data = get_url_report(url)
        case 'kp':
            data = looking_web_address(url)
        case _:
            pass

    if data['status'] == 'ok' and not update:
        status = insertUrlData(data['data'], engine)
    elif update:
        status = updateUrlData(url, engine, data['data'])

    close_db()
    if data['status'] == 'error':
        status = {'status': data['status'], 'msg': data['msg']}
    data = data['data']

    return [data, status]


def delete_all_files():
    status = deleteAllFileData()
    return status


def delete_all_urls():
    status = deleteAllUrlsData()
    return status

# def scan_file(url: str, engine: str = 'vt'):
#     pass


# def scan_url():
#     pass
