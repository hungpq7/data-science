from json import (
    loads as load_json,
    dumps as dump_json,
)

from yaml import (
    safe_load as load_yaml,
    dump as dump_yaml,
)

def read_text(path):
    content = None
    try:
        file = open(path)
        content = file.read()
        file.close()
    except:
        import requests
        response = requests.get(path)
        content = response.text
    finally:
        if content is None:
            raise Exception(f'Path {path} not found')
        else:
            return content