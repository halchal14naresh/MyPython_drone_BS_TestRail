import logging
import re

from selenium import webdriver

from selenium_base.path import GetPath
from utilities.generic_functions import GenericFunctions
from utilities.logger import customLogger


class CaptureScreenShot:

    @staticmethod
    def capture_screenshot(driver: webdriver, title: str):
        """
        This method captures screenshot and copied it at given location.
        """
        try:
            log = customLogger(logging.INFO)
            log.info("Capturing the screen shot of failed test case '" + title + "'.")
            # Get path of screen shot folder
            paths = GetPath()
            os = GenericFunctions.get_os()
            screenshot_folder = paths.screenshot_folder_path()

            # create screenshot name using title and timestamp
            # current_date = "_".join(re.split(" |\:|\.", str(GenericFunctions.get_current_date_time())))
            current_date = GenericFunctions.get_filename_datetimestamp()
            if os.casefold() == 'windows':
                screenshot_name = "\\" + title + "_" + current_date + ".png"
            else:
                screenshot_name = "/" + title + "_" + current_date + ".png"
            screenshot_path = screenshot_folder + screenshot_name
            log.info("Screenshot path: " + screenshot_path)

            if driver is not None:
                driver.save_screenshot(screenshot_path)
            else:
                log.error("Driver is None ")
        except Exception as e:
            log.error("Capture Screenshot exception: " + str(e))
        return screenshot_path
