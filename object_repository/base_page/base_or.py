"""
This class will be base class for all page object classes
"""
import logging

from object_repository.base_page.base_enum import BaseEnum
from selenium_base.selenium_utils import SeleniumUtils
from utilities.logger import customLogger


class BasePageOR:
    """
    Elements for this page is defined in base_enum

    """
    log = customLogger(logging.INFO)

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        self.actions = SeleniumUtils(self.driver, self.log)

    def is_error_displayed(self):
        return self.actions.is_element_present(BaseEnum.ERROR_MESSAGE.value[0], BaseEnum.ERROR_MESSAGE.value[1])
