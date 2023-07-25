import os
import requests
from requests.exceptions import HTTPError
from dotenv import load_dotenv

from .variables.var_kp import (
    atrs_url_4_UrlDomainWhoIs,
    atrs_file_4_FileGeneralInfo,
    atrs_url_4_UrlGeneralInfo
)

load_dotenv()

API_KEY = os.getenv('KASPERSKY_API_KEY')

def filter_data_4_file(data, atrs):
    """
    atrs -- FileGeneralInfo
    """
    res = {}
    for key, value in data.items():
        if key == "FileGeneralInfo":
            for k, v in value.items():
                if k in atrs:
                    res[k.lower()] = v
        elif key == 'DetectionsInfo':
            res['DetectionsInfo'] = data[key]
    return res


def filter_data_4_url(data, atrs1, atrs2):
    """
    atrs1 -- UrlGeneralInfo
    atrs2 -- UrlDomainWhoIs    
    """
    res = {}
    try:
        UrlGeneralInfo = data['UrlGeneralInfo']
        for key, value in UrlGeneralInfo.items():
            if key in atrs1:
                res[key.lower()] = value
    except KeyError:
        pass
    try:
        UrlDomainWhoIs = data['UrlDomainWhoIs']
        for key, value in UrlDomainWhoIs.items():
            if key in atrs2:
                res[key.lower()] = value
    except KeyError:
        pass
    return res


def looking_hash_file(hash: str):
    res = {}
    try:
        response = requests.get(f"https://opentip.kaspersky.com/api/v1/search/hash?request={hash}",
                                headers={"x-api-key": API_KEY})
        response.raise_for_status()
        if response.status_code == 200:
            data = filter_data_4_file(
                response.json(), atrs_file_4_FileGeneralInfo)
            res = {"status": "ok", "data": data}
        else:
            res = {"status": "error",
                   "msg": "Documento no encontrado en Kaspersky", "data": {}}
    except HTTPError as e:
        res = {"status": "error",
               "msg": "No hay respuesta del servidor", "data": {}}
    finally:
        return res


def looking_web_address(url: str):
    res = {}
    try:
        response = requests.get(f"https://opentip.kaspersky.com/api/v1/search/url?request={url}",
                                headers={"x-api-key": API_KEY})
        # print(response.status_code)
        # response.raise_for_status()
        if response.status_code == 200:
            data = filter_data_4_url(
                response.json(), atrs_url_4_UrlGeneralInfo, atrs_url_4_UrlDomainWhoIs)
            res = {"status": "ok", "data": data}
        else:
            res = {"status": "error",
                   "msg": "URI no encontrado en Kaspersky", "data": {}}
    except HTTPError as e:
        res = {"status": "error",
               "msg": "No hay respuesta del servidor", "data": {}}
    finally:
        return res
