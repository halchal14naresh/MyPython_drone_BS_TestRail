from selenium.common.exceptions import *
from selenium.webdriver.common.by import By


class BrowserActions:

    def __init__(self, driver, log):
        self.log = log
        if driver is not None:
            self.driver = driver
        else:
            self.log.error("Driver is None")
            raise Exception("Driver is None")

    def get_locator_type(self, locator_type: str):
        """
        This method returns the locator strategy (By class),
        basis on provided locator type. Expected locator types:
        id, name, xpath, class name, css, link text, partial
        link text and tag name
        """
        locator_type = locator_type.casefold()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "class name":
            return By.CLASS_NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partial link":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "tag name":
            return By.TAG_NAME
        else:
            self.log.error("Invalid locator type")
            return None

    def get_element(self, locator: str, locator_type: str):
        """
        This metohd accepts two string parameters, locator_type and locator.
        On the basis of parameter it search and returns an element if found
        in DOM else throws exception.
        """
        try:
            by_type = self.get_locator_type(locator_type=locator_type)
            if by_type is not None:
                return self.driver.find_element(by_type, locator)
            else:
                raise InvalidSelectorException
        except Exception as msg:
            self.log.error("Exception: " + str(msg))
            return None

    def get_elements(self, locator: str, locator_type: str):
        """
        This method accepts two string parameters, locator_type and locator.
        On the basis of parameter it search and returns an element if found
        in DOM else throws exception.
        """
        try:
            by_type = self.get_locator_type(locator_type=locator_type)
            if by_type is not None:
                elements = self.driver.find_elements(by_type, locator)
                return elements
            else:
                raise InvalidSelectorException
        except Exception as e:
            self.log.error("Exception: " + str(e))
            return None

    def send_url(self, url: str) -> None:
        """
        Open AUT using url
        """
        self.driver.get(url)

    def click_element(self, locator: str, locator_type: str) -> None:
        """
        Click on given element.
        """
        try:
            self.get_element(locator=locator, locator_type=locator_type).click()
        except Exception as e:
            self.log.error("Exception - click_element " + str(e))
            self.log.error("Element " + locator)
            raise

    def click_elements_index(self, locator: str, locator_type: str, index: int) -> None:
        """
        Click given index element.
        """
        elements = None
        try:
            elements = self.get_elements(locator=locator, locator_type=locator_type)
            elements[index].click()
        except Exception as e:
            self.log.error("Exception - click_element " + str(e))
            self.log.error("Element " + locator)
            raise

    def click_elements_value(self, locator: str, locator_type: str, value: str) -> None:
        """
        Click element of given index.
        """
        try:
            elements = self.get_elements(locator=locator, locator_type=locator_type)
            for element in elements:
                if element.text.casefold() == value.casefold():
                    element.click()
        except Exception as e:
            self.log.error("Exception - click_element " + str(e))
            self.log.error("Element " + locator)
            raise

    def click_elements_attribute_value(self, locator: str, locator_type: str, attribute: str,
                                       attribute_value: str) -> None:
        """
        Click element which has matching attribute_value
        """
        elements = None
        try:
            elements = self.get_elements(locator=locator, locator_type=locator_type)
            for element in elements:
                if attribute_value.casefold() in element.get_attribute(attribute).casefold():
                    self.log.info("Click element which has matching attribute_value: "+attribute_value)
                    element.click()
                    break
        except Exception as e:
            self.log.error("Exception - click_element " + str(e))
            self.log.error("Element " + locator)
            raise

    def submit_element(self, locator: str, locator_type: str) -> None:
        """
        Press Submit button on Element
        """
        try:
            self.get_element(locator=locator, locator_type=locator_type).submit()
        except Exception as e:
            self.log.error("Exception - enter_text " + str(e))
            self.log.error("Element " + locator)
            raise

    def enter_text(self, locator: str, locator_type: str, value: str) -> None:
        """
        Enter given text in given field.
        """
        try:
            self.get_element(locator=locator, locator_type=locator_type).send_keys(value)
        except Exception as e:
            self.log.error("Exception - enter_text " + str(e))
            self.log.error("Element " + locator)
            raise

    def enter_text_elements_index(self, locator: str, locator_type: str, index: int, value: str) -> None:
        """
        Enter the given text in text box selected using index number.
        """
        try:
            elements = self.get_elements(locator=locator, locator_type=locator_type)
            elements[index].send_keys(value)
        except Exception as e:
            self.log.error("Exception - enter_text " + str(e))
            self.log.error("Element " + locator)
            raise

    def get_text_from_list(self, locator: str, locator_type: str):
        """
        return the list of text for the list of elements
        """
        try:
            element_text_list = []
            element_list = self.get_elements(locator=locator, locator_type=locator_type)
            for element in element_list:
                element_text_list.append(element.text)

            return element_text_list
        except Exception as e:
            self.log.error("Exception - get_text_from_list " + str(e))
            self.log.error("Element " + locator)
            raise

    def get_text(self, locator: str, locator_type: str):
        """
        return the list of text for the list of elements
        """
        element = None
        try:
            element = self.get_element(locator=locator, locator_type=locator_type)
            return element.text
        except Exception as e:
            self.log.error("Exception - get_text_from_list " + str(e))
            self.log.error("Element " + locator)
            raise

    def get_text_elements_index(self, locator: str, locator_type: str, index:int):
        """
        return the text of element of given index
        """
        element = None
        try:
            elements = self.get_elements(locator=locator, locator_type=locator_type)
            return elements[index].text
        except Exception as e:
            self.log.error("Exception - get_text_from_list " + str(e))
            self.log.error("Element " + locator)
            raise

    def quit_browser(self):
        """
        quit browser
        """
        try:
            self.driver.quit()
        except Exception as e:
            self.log.error("Exception - quit_browser " + str(e))
            raise

    def is_element_present(self, locator: str, locator_type: str) -> bool:
        """return true if given element found on page"""
        if self.get_element(locator=locator, locator_type=locator_type):
            return True
        else:
            return False

    def is_element_present_list(self, locator: str, locator_type: str, index:int) -> bool:
        """return true if given element found on page"""
        elements = self.get_elements(locator=locator, locator_type=locator_type)
        if elements[index]:
            return True
        else:
            return False

    def get_element_attribute(self, locator: str, locator_type: str, attribute: str) -> str:
        """
        return the attribute value for the given element
        """
        try:
            return self.get_element(locator=locator, locator_type=locator_type).get_attribute(attribute)
        except Exception as e:
            self.log.error("Exception - get_elenemt_attribute " + str(e))
            self.log.error("Element " + locator)
            raise

    def get_element_attribute_of_index(self, locator: str, locator_type: str, attribute: str, index: int) -> str:
        """
        return the attribute value for the given element
        """
        try:
            elements = self.get_elements(locator=locator, locator_type=locator_type)
            return elements[index].get_attribute(attribute)
        except Exception as e:
            self.log.error("Exception - get_elenemt_attribute " + str(e))
            self.log.error("Element " + locator)
            raise

    def is_attribute_present(self, locator: str, locator_type: str, attribute: str):
        try:
            element = self.get_element(locator=locator, locator_type=locator_type)
            if element.get_attribute(attribute) is not None:
                return True
            else:
                return False
        except Exception as e:
            self.log.error("Exception - is_attribute_present " + str(e))
            self.log.error("Element " + locator)
            raise

    def is_attribute_present_elements(self, locator: str, locator_type: str, index: int, attribute: str):
        try:
            elements = self.get_elements(locator=locator, locator_type=locator_type)
            if elements[index].get_attribute(attribute) is not None:
                return True
            else:
                return False
        except Exception as e:
            self.log.error("Exception - is_attribute_present " + str(e))
            self.log.error("Element " + locator)
            raise

    def clear_text_field(self, locator: str, locator_type: str) -> str:
        """
        clearing entered text in text fields
        """
        element = self.get_element(locator, locator_type)
        element.clear()
