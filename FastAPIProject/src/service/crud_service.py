from pymongo import MongoClient
from fastapi import Response, status
import src.utils.service_constants as constants
from src.utils.log_util import logger
import json


mongodb_url = "mongodb://localhost:27017"
connection = MongoClient(mongodb_url)
db = connection["testdb"]


def read():
    # Response object
    response = Response()
    del response.headers["content-length"]
    response.headers["content-type"] = constants.CONTENT_TYPE
    response_body = {}

    try:
        collection = db["test"]
        data = []
        for row in collection.find():
            row["_id"] = str(row["_id"])
            data.append(row)
        if data:
            response_body["message"] = "Details"
            response_body["data"] = data
            response.body = json.dumps(response_body).encode()
            response.status_code = status.HTTP_200_OK
        else:
            response_body["message"] = "Data not found"
            response.body = json.dumps(response_body).encode()
            response.status_code = status.HTTP_204_NO_CONTENT

    except Exception as e:
        logger.info(str(e))
        response_body["message"] = str(e)
        response.body = json.dumps(response_body).encode()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        # Closing the db connection
        connection.close()

    return response


