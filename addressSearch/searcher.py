def find_match_address(req_body, json_database):

    search_result = []
    
    try:
        countries = req_body['searchCountries'].lower().strip().split(' ')
    except:
        return []

    if not(countries):
        return []

    for address in json_database:

        isValid = True

        if(address['Country'].lower() not in countries):
            continue

        for key in req_body:
            try:
                if(req_body[key].strip().lower() != address[key].strip().lower()):
                    isValid = False
                    break
            except:
                continue

        if(isValid):
            search_result.append(address)

    return search_result