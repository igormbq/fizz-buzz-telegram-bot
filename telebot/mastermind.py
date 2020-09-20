def get_response(msg):
    if type(msg) and len(msg) <= 280:
        return f'valid'
    else:
        return f'invalid entry'

    return "foi 999!!!"