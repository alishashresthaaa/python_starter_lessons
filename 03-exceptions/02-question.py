# Extending Exception for CustomExceptionError
class CustomExceptionError(Exception):
    # Constructor init
    def __init__(self, message, time_crashed):
        self.message = message
        self.crashed_time = time_crashed
        super().__init__(message)

try:
    print("Line One")
    print("Line Two")
    raise CustomExceptionError("This is custom error message", datetime.now())
except CustomExceptionError as e:
    print(e.message)
    print("Crashed happened at: ", e.crashed_time)
finally:
    print("Inside Finally")
