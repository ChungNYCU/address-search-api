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

        if address['Country'].lower() not in countries:
            continue

        for key in req_body:
            try:
                if req_body[key] and address[key]:
                    if type(req_body[key]) == str:
                        if req_body[key].strip().lower() != address[key].strip().lower():
                            isValid = False
                            break
                    elif type(req_body[key]) == int:
                        if req_body[key] != address[key]:
                            isValid = False
                            break
                elif req_body[key] and not address[key]:
                    isValid = False
                else:
                    continue
            except:
                continue

        if isValid:
            search_result.append(address)

    return search_result