import os
from dotenv import load_dotenv
import vt

from .variables.var_vt import atrs_file, atrs_url

load_dotenv()
API_KEY = os.environ['VIRUSTOTAL_API_KEY']


def open_conn() -> vt.Client:
    return vt.Client(apikey=API_KEY)


def close_conn(client: vt.Client) -> None:
    client.close()


def filter_data(data, atrs):
    res = {}
    for key, value in data.items():
        if key in atrs:
            if key == 'last_analysis_results':
                lar = []
                for k in data['last_analysis_results'].keys():
                    category = data['last_analysis_results'][k]['category']
                    if category != 'undetected':
                        lar.append({k: data['last_analysis_results'][k]})
                res['last_analysis_results'] = lar
                continue
            res[key] = value
    return res


def get_file_report(hash: str):
    client = open_conn()
    res = {}
    try:
        data = client.get_json('/files/{}', hash)['data']['attributes']
        res = {"status": "ok", "data": filter_data(data, atrs_file)}

    except vt.error.APIError as e:
        if (e.args[0] == 'NotFoundError'):
            res = {"status": "error",
                   "msg": "Documento no Econtrado en VirusTotal",
                   "exeption": e.args, "data": {}}
    except KeyError as ke:
        print(ke.args)
    finally:
        close_conn(client)
        return res


def get_url_report(url: str):
    client = open_conn()
    res = {}
    try:
        url_id = vt.url_id(url=url)
        data = client.get_json("/urls/{}", url_id)['data']['attributes']
        res = {"status": "ok", "data": filter_data(data, atrs_url)}

    except vt.error.APIError as e:
        if (e.args[0] == 'NotFoundError'):
            res = {"status": "error",
                   "msg": "URI no Econtrado en VirusTotal",
                   "exeption": e.args, "data": {}}
    finally:
        close_conn(client)
        return res


# def upload_file():
#     pass

# def upload_url():
#     pass

# get_url_report("http://cioco-froll.com/")

# data = get_file_report("25c77d35b685b78017ed7830873e065a")
# data = get_file_report(
#     "4208C9A483CCB123F76CD0A77CAD0D5EA3A12930D0C4832832A75BEB1092EC0A")

# print(data)
