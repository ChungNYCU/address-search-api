def find_match_address(req_body, json_database):

    search_result = []

    for address in json_database:
        isValid = True
        for key in req_body:
            if(address[key].strip().lower() != req_body[key].strip().lower()):
                isValid = False
                break
        if(isValid):
            search_result.append(address)

    return search_result