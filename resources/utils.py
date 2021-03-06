def fizz_buzz(msg):
    # Validation to verify if is a valid number
    number = validate_data(msg)
    """
    Return a response based on the input, following the Fizzbuzz logic:
    Number is multiple of 3 and 5 then is 'fizbuzz'
    Number is multiple of 3 then is 'fizz'
    Number is multiple of 5 then is 'buzz'
    Number is not a multiple of 5 or 3 then return the entry number

    :param number: Integer number typed by the user.
    """
    if (number % 3 == 0) and (number % 5 == 0):
        return "{} is fizzbuzz".format(number)
    if number % 3 == 0:
        return "{} is fizz".format(number)
    if number % 5 == 0:
        return "{} is buzz".format(number)
    else:
        return number


def validate_data(msg):
    """
    This function verify if the entry is up to 280 characters
    and it's is a integer number If you meet these condition
    passes the value to the fizz_buzz function, otherwise,
    return the correct entry instruction to the user

    :param msg: Entry typed by the chatbot user.
    """
    if (len(msg) <= 280) and (msg.isdecimal()):
        return int(msg)
    else:
        return "Your entry must be an integer number and not more than 280 characters"
