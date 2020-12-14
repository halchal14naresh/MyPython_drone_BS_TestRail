import logging

from object_repository.base_page.base_or import BasePageOR
from object_repository.deskboard_section.deskboard_enum import DeskBoardEnum
from utilities.logger import customLogger


class DeskBoardOR(BasePageOR):
    """
    this is Object repository of Header Section
    """

    log = customLogger(logging.INFO)

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        super().__init__(driver=self.driver, log=self.log)

    def google_search_box_set_value(self, text):
        self.actions.enter_text(DeskBoardEnum.searchBox.value[0], DeskBoardEnum.searchBox.value[1], text)
        self.actions.submit_element(DeskBoardEnum.searchBox.value[0], DeskBoardEnum.searchBox.value[1])
