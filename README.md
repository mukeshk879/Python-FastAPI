# Python-FastAPI

import json
from fastapi import FastAPI

import logging

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)


@app.get('/fast_api/test')
def test():
    logging.info("Logs ********************************************")
    data = {"id": "123456",
            "name": "Mukesh Kumar"
            }
    return json.dumps(data)


