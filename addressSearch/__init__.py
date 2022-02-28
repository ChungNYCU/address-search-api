import azure.functions as func
import json
import logging
import pathlib

from addressSearch import searcher


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except Exception as e:
        return func.HttpResponse("Cannot get req_body: " + str(e), status_code=400)

    try:
        path = pathlib.Path(__file__).parent / 'addresses.json'
        f = open(path)
    except Exception as e:
        return func.HttpResponse("Cannot access database: " + str(e), status_code=400)

    try:
        data = json.load(f)
    except Exception as e:
        return func.HttpResponse("Cannot load database: " + str(e), status_code=400)

    try:
        search_result = searcher.find_match_address(req_body, data)
    except Exception as e:
        return func.HttpResponse("Cannot search address: " + str(e), status_code=400)

    
    return func.HttpResponse(json.dumps(search_result), status_code=200)
