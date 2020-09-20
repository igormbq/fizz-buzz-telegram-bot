def validate_data(data):
    if len(data) <= 280 and isinstance(data, int):
        print("valid integer")
        return True
    else:
        print("The maximum number of characters is 280 and must be an integer")
        return False

def fizzbuzz(value):
    if (value % 3 == 0) and (value % 5 == 0):
        print("{} é FizzBuzz".format(value))
    if (value % 3 == 0):
        print("{} é Fizz".format(value))
    if (value % 5 == 0):
        print("{} é Buzz".format(value))
    else:
        print(value)
