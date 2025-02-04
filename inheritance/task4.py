from datetime import datetime


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("logs.txt", "a") as log_file:
            log_file.write(msg + f" {current_datetime} " + "\n")


try:
    raise CustomException("This is a custom error message")
except CustomException as error:
    print(f"Error: {error}")


