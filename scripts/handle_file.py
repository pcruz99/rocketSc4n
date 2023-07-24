from hashlib import md5, sha1, sha256

def get_file_hash(path:str, hash_alg:str):
    file_hash = ''
    try:            
        with open(path,'rb') as file:
            data = file.read()
            match hash_alg:
                case 'md5':
                    file_hash = md5(data).hexdigest()
                case 'sha1':
                    file_hash = sha1(data).hexdigest()
                case 'sha256':
                    file_hash = sha256(data).hexdigest()
                case _:
                    raise Exception
    except Exception:
        pass
    return file_hash