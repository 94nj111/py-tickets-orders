def params_to_int(query_string):
    return [int(el) for el in query_string.split(",")]
