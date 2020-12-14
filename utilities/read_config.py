import configparser
import logging

from selenium_base.path import GetPath
from utilities.generic_functions import GenericFunctions
from utilities.logger import customLogger


class ReadConfig:
    log = customLogger(logging.INFO)

    def get_config_file(self):
        """
        Get config.ini
        """
        try:
            paths = GetPath()
            config_file_path = paths.config_path()
            config = configparser.RawConfigParser()
            config.read(config_file_path)
            return config
        except Exception as e:
            self.log.error("Error while reading config.ini file" + str(e))
            return None

    def get_property_value(self, section: str, key: str) ->str:
        """
        Returns property value for give key.
        If key is password first it decrypt the encrypted password and return it
        """
        try:
            config = self.get_config_file()
            value = config.get(section, key)
            if 'password' in key.casefold():
                decrypt_key = (config.get(section, key + "_key"))
                password = GenericFunctions.decrypt_value(decrypt_key, value)
                if password is not None:
                    return password
                else:
                    raise Exception ("Password Key is None. Please check password key is valid or not.")

            else:
                return value
        except Exception as e:
            self.log.error("Error while reading config.ini file" + str(e))
            return None
