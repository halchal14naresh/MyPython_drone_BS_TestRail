import logging

import pytest
import softest

from object_repository.deskboard_section.deskboard_or import DeskBoardOR
from utilities.logger import customLogger
from utilities.read_config import ReadConfig


@pytest.mark.usefixtures("one_time_setup", "class_level_setup", "setup")
class TestGetDetails(softest.TestCase):
    log = customLogger(logging.INFO)

    @pytest.fixture(autouse=True)
    def class_level_setup(self, class_level_setup):
        self.read_prop = ReadConfig()
        url = self.read_prop.get_property_value("QA_ENVIRONMENT", "application_url")
        print("application_url is", url)
        self.driver.get(url)
        print("application_url is Opened now ", url)

    @pytest.mark.smoke
    def test_method_cybage(self):
        obj = DeskBoardOR(self.driver, self.log)
        obj.google_search_box_set_value("Cybage")
        print(self.driver.title)

    @pytest.mark.smoke
    def test_method_selenium(self):
        obj = DeskBoardOR(self.driver, self.log)
        obj.google_search_box_set_value("selenium")
        print(self.driver.title)

    @pytest.mark.smoke
    def test_method_python(self):
        obj = DeskBoardOR(self.driver, self.log)
        obj.google_search_box_set_value("python")
        print(self.driver.title)
