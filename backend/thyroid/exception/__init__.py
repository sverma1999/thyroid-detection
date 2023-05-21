import sys
from backend.thyroid.logger import logging


def error_message_detail(error, error_detail: sys):
    # Retrieving the old-style representation of the handled exception
    # we only need traceback object in exc_tb variable
    _, _, exc_tb = error_detail.exc_info()

    # Getting the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Constructing the error message with script name, line number, and error message
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # Returning the error message
    return error_message


class Custom_Exception(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Calling the super class constructor to get inherited properties of the error
        super().__init__(error_message)
        # Constructing the error message
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        # Returning the error message
        return self.error_message


# For testing purpose only
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("DIVIDE BY ZERO ERROR")
#         raise Custom_Exception(e, sys)
