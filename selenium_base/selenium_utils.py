from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium_base.wait_utlity import WaitForElement
from utilities.generic_functions import GenericFunctions


class SeleniumUtils(WaitForElement):
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        WaitForElement.__init__(self, driver, log)

    def get_element_location_size(self, locator: str, locator_type: str) -> list:
        location_size = []
        element = self.get_element(locator=locator, locator_type=locator_type)
        location = element.location
        size = element.size
        location_size.append(location)
        location_size.append(size)
        return location_size

    def select_element(self, locator: str, locator_type: str) -> object:
        """
        Returns Select class variable.
        """
        return Select(self.get_element(locator=locator, locator_type=locator_type))

    def select_using_index(self, locator: str, locator_type: str, index: int) -> None:
        """
        Select the option at the given index.
        """
        select = self.select_element(locator, locator_type)
        select.select_by_index(index)

    def select_using_value(self, locator: str, locator_type: str, value: str) -> None:
        """
        Select all options that have a value matching the argument.
        """
        select = self.select_element(locator, locator_type)
        select.select_by_value(value)

    def select_using_visible_text(self, locator: str, locator_type: str, visible_text: str) -> None:
        """
        Select all options that display text matching the argument
        """
        select = self.select_element(locator, locator_type)
        select.select_by_visible_text(visible_text)

    def scroll_to_element(self, locator: str, locator_type: str):
        """
        Scroll till the given element so that element should be present in view.
        """
        actions = ActionChains(self.driver)
        element = self.get_element(locator,locator_type)
        actions.move_to_element(element)
        actions.perform()

    def scroll_to_elements_by_inidex(self,locator: str, locator_type: str, index: int):
        """
        Scroll till the given element so that element should be present in view.
        """
        actions = ActionChains(self.driver)
        elements = self.get_elements(locator, locator_type)
        actions.move_to_element(elements[index])
        actions.perform()

    def scroll_to_element_js(self, locator: str, locator_type: str):
        """
        Scroll till the given element using java script.
        """
        element = self.get_element(locator, locator_type)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_to_elements_js(self, locator: str, locator_type: str, index: int):
        """
        Scroll till the given element using java script.
        """
        elements = self.get_elements(locator, locator_type)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', elements[index])

    def get_page_title(self) -> str:
        """
        returns the title of page
        """
        return self.driver.title