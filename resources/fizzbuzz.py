def validate_data(text):
    if (len(text) <= 280) and (text.isdecimal()):
        fizz_buzz(int(text))
    else:
        return "Your entry must be an integer number and not more than 280 characters"


def fizz_buzz(value):
    if (value % 3 == 0) and (value % 5 == 0):
        return "{} is FizzBuzz".format(value)
    if value % 3 == 0:
        return "{} is Fizz".format(value)
    if value % 5 == 0:
        return "{} is Buzz".format(value)
    else:
        return value