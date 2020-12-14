"""
This module have generic functions like data related functions,
string operation related functions etc.
"""
import datetime
import os.path
import platform
import re
import shutil
from datetime import date

from utilities.encrypt_decrypt import EncryptDecrypt


class GenericFunctions:

    @staticmethod
    def get_current_date_time() -> object:
        """This method return current date with time stamp
        like 2020-09-17 10:16:36.311744"""
        return datetime.datetime.now()

    @staticmethod
    def get_current_date() -> object:
        """This method return current date with time stamp
        like 2020-09-17"""
        return date.today()

    @staticmethod
    def get_filename_date():
        current_date = str(GenericFunctions.get_current_date())
        file_name = "_".join(current_date.split("-"))
        return file_name

    @staticmethod
    def get_filename_datetimestamp():
        file_name = "_".join(re.split(" |\:|\.", str(GenericFunctions.get_current_date_time())))
        return file_name

    @staticmethod
    def get_os():
        """
        Return OS of system
        """
        os = platform.system()
        return os

    @staticmethod
    def isdir_present(dir_path, dirname=None):
        if os.path.isdir(dir_path):
            pass
        else:
            if dirname is not None:
                path = os.path.join(dir_path, dirname)
            else:
                path = dir_path
            os.mkdir(path)

    @staticmethod
    def move_directories(source: str, destination: str):
        shutil.move(source, destination)

    @staticmethod
    def decrypt_value(de_key, de_value):
        try:
            dec_enc = EncryptDecrypt()
            encrypted = bytes(de_value, 'utf8')
            return dec_enc.decrypt_message(encrypted,de_key)
        except Exception as msg:
            print("ERROR: "+str(msg))
            return None

