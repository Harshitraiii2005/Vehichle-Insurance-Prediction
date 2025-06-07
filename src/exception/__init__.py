import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """
    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        # No traceback info available, likely manually raised exception
        file_name = "Unknown file"
        line_number = "Unknown line"
    else:
        # Get the file name and line number where the exception occurred
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

    # Create a formatted error message string with file name, line number, and the actual error
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    # Log the error for better tracking
    logging.error(error_message)
    
    return error_message


class MyException(Exception):
    """
    Custom exception class for handling errors.
    """
    def __init__(self, error_message: str, error_detail: sys):
        """
        Initializes the exception with a detailed error message.

        :param error_message: A string describing the error.
        :param error_detail: The sys module to access traceback details.
        """
        # Format the detailed error message using the error_message_detail function
        detailed_message = error_message_detail(error_message, error_detail)
        super().__init__(detailed_message)
        self.error_message = detailed_message

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message
