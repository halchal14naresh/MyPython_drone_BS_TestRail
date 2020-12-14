import inspect
import logging

from selenium_base.path import GetPath
from utilities.generic_functions import GenericFunctions


def customLogger(log_level):
    """
    Create logger which status like Info, Error, Critical etc.
    """
    logger = None
    try:
        # getting the logs folder path + creating file name
        # with current datetime stamp
        paths = GetPath()
        log_path = paths.log_file_path()
        file_name = GenericFunctions.get_filename_date()
        if 'windows' in GenericFunctions.get_os().casefold():
            file_path = log_path + "\\" + "Automation_" + file_name
        else:
            file_path = log_path + "/" + "Automation_" + file_name

        # Gets the name of the class / method from where
        # this method is called
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # By default, log all messages
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(file_path + ".log", mode='a')
        file_handler.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s'
                                      ' - %(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        print(e)

    return logger
