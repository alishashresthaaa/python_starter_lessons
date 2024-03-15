# Custom Exception class
class CustomExceptionError(Exception):
    pass

try:
    print("Line One")
    print("Line Two")
    raise CustomExceptionError
except:
    print("Catching custom exception")
finally:
    print("Inside Finally")
