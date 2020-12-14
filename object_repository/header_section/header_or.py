from object_repository.base_page.base_or import BasePageOR
from utilities.logger import customLogger
import logging


class HeaderPage(BasePageOR):
    """
    this is Object repository of Header Section
    """

    log = customLogger(logging.INFO)

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        super().__init__(driver=self.driver, log=self.log)
