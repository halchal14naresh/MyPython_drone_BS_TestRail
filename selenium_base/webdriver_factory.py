import logging

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from utilities.logger import customLogger
from utilities.read_config import ReadConfig

readProp = ReadConfig()


class DriverFactory():
    log = customLogger(logging.INFO)

    def driver_initialize(self, browser: str, test_name: str = None):
        """
        This method initialize web driver of provided browser.
        And Maximize the browser window.

        :return: webdriver
        """
        global readProp
        try:
            if browser is not None:
                browser = browser.casefold()
            default = "Incorrect browser name"
            return getattr(self, 'init_' + browser, lambda: default)()
        except Exception as e:
            self.log.error("Driver error: " + str(e))
        return None

    # def desired_capabilities(self, test_name: str):
    #     desired_cap = {}
    #     # 'os_version': '8.1',
    #     # 'resolution': '1920x1080',
    #     # 'browser': 'Firefox',
    #     # 'browser_version': 'latest',
    #     # 'os': 'Windows',
    #     # 'name': test_name,  # test name
    #     # 'browserstack.debug': False
    #     # # 'build': 'BStack Build Number 1'  # CI/CD job or build name
    #     # }
    #     desired_cap.update(resolution=readProp.get_property_value('CAPABILITIES', "resolution"))
    #     desired_cap.update(browser=readProp.get_property_value('CAPABILITIES', "browser"))
    #     desired_cap.update(os=readProp.get_property_value('CAPABILITIES', "os"))
    #     desired_cap.update(name=test_name)
    #     return desired_cap

    def desired_capabilities(self):
        desired_cap = {}
        desired_cap.update(os=readProp.get_property_value('CAPABILITIES', "os"))
        desired_cap.update(os_version=readProp.get_property_value('CAPABILITIES', "os_version"))
        desired_cap.update(resolution=readProp.get_property_value('CAPABILITIES', "resolution"))
        desired_cap.update(browser=readProp.get_property_value('CAPABILITIES', "browser"))
        desired_cap.update(browser_version=readProp.get_property_value('CAPABILITIES', "browser_version"))
        desired_cap.update(name=readProp.get_property_value('CAPABILITIES', "name"))
        desired_cap.update(build=readProp.get_property_value('CAPABILITIES', "build"))
        return desired_cap

    def init_firefox(self):
        self.log.info("Launching FireFox browser")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver

    def init_chrome(self):
        self.log.info("Launching Chrome browser")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # NOTE: Use above code to initialize chrome driver. Below code for chrome driver is temporary
        # driver = webdriver.Chrome(executable_path="D:\\PDS\\Automation\\PDSF_Automation\\drivers\\chromedriver.exe")
        # driver = webdriver.Chrome(executable_path="/home/nareshy/pythonAutomation/PDSF_Automation/drivers/chromedriver.exe")

        driver.maximize_window()
        return driver

    def init_ie(self):
        self.log.info("Launching Internet Explorer browser")
        driver = webdriver.Ie(IEDriverManager().install())
        driver.maximize_window()
        return driver

    def init_lambdatest(self, test_name):
        # Lambda Test tool code
        username = readProp.get_property_value('LAMBDA_TEST', "username")
        access_key = readProp.get_property_value('LAMBDA_TEST', "access_key")
        selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
        executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
        driver = webdriver.Remote(command_executor=executor, desired_capabilities=self.desired_capabilities(test_name))

        # Borwoserstack code
        # driver = webdriver.Remote(
        #     command_executor='https://nileshyeole1:hdcYVD1dNJV4e8sNn6tG@hub-cloud.browserstack.com/wd/hub',
        #     desired_capabilities=self.desired_capabilities(test_name))
        return driver

    def init_bs(self):
        self.log.info("Launching  browser in Browser Stack")
        print("Launching  browser in Browser Stack")
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Remote(
            command_executor='https://testuser1319:kqwyxq2TqmGvA5zYNyXp@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=self.desired_capabilities())
        return driver
