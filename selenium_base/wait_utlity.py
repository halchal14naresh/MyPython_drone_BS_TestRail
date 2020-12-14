from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from selenium_base.browser_actions_wrapper import BrowserActions


class WaitForElement(BrowserActions):
    # log = customLogger(logging.INFO)

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        BrowserActions.__init__(self, driver, log)

    def prepare_wait(self, time: int = 10, poll_frequency: float = .5):
        """
        Return wait object.
        """
        return WebDriverWait(self.driver, time, poll_frequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

    def wait_for_element_to_be_clickable(self, locator: str, locator_type: str, time=10):
        """
        An Expectation for checking an element is visible and enabled such that
    you can click it.

        """
        element = None
        wait = self.prepare_wait(time)
        try:
            by_type = self.get_locator_type(locator_type=locator_type)
            element = wait.until(expected_conditions.element_to_be_clickable((by_type, locator)))
        except Exception as msg:
            self.log.error("Error at element_to_be_clickable: " + str(msg))

        return element

    def wait_to_element_visible(self, locator: str, locator_type: str, time=10):
        """An expectation for checking that an element is present on the DOM of a
            page and visible. Visibility means that the element is not only displayed
            but also has a height and width that is greater than 0.
            locator - used to find the element
            returns the WebElement once it is located and visible
        """
        element = None
        wait = self.prepare_wait(time)
        try:
            by_type = self.get_locator_type(locator_type=locator_type)
            element = wait.until(expected_conditions.visibility_of_element_located((by_type, locator)))
        except Exception as msg:
            self.log.error("Error at wait_to_element_visible: " + str(msg))

        return element

    def wait_to_element_invisible(self, locator: str, locator_type: str):
        """ An Expectation for checking that an element is either invisible or not
            present on the DOM.
            element is either a locator (text) or an WebElement
            """
        element = None
        wait = self.prepare_wait()
        try:
            by_type = self.get_locator_type(locator_type=locator_type)
            element = wait.until(expected_conditions.invisibility_of_element_located((by_type, locator)))
        except Exception as msg:
            self.log.error("Error at wait_to_element_invisible: " + str(msg))

        return element

    def wait_till_attribute_changes(self, locator: str, locator_type: str, attribute: str,
                                    expected_attribute_value: str):
        """
        Wait till given attribute does not have expected value
        """
        try:
            actual_attribute_value = self.get_element_attribute(locator=locator, locator_type=locator_type,
                                                                attribute=attribute)
            if expected_attribute_value.casefold() not in actual_attribute_value.casefold():
                self.wait_till_attribute_changes(locator, locator_type, attribute, expected_attribute_value)
            else:
                pass
        except Exception as msg:
            self.log.error("Error: " + str(msg))
            raise

    def wait_till_attribute_changes_by_index(self, locator: str, locator_type: str, attribute: str,
                                             expected_attribute_value: str, index: int):
        """
        Wait till given attribute does not have expected value
        """
        try:
            actual_attribute_value = self.get_element_attribute_of_index(locator=locator, locator_type=locator_type,
                                                                         attribute=attribute, index=index)
            if expected_attribute_value.casefold() not in actual_attribute_value.casefold():
                self.wait_till_attribute_changes_by_index(locator, locator_type, attribute, expected_attribute_value,
                                                          index)
            else:
                pass
        except Exception as msg:
            self.log.error("Error: " + str(msg))
            raise
