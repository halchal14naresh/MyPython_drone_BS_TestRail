"""
This is the start point for test case execution
"""

import logging

import allure
import pytest
from allure_commons.types import AttachmentType

from object_repository.header_section.header_or import HeaderPage
from object_repository.login_page.login_page_or import LoginPageOR
from selenium_base.path import GetPath
from selenium_base.take_screenshot import CaptureScreenShot
from selenium_base.webdriver_factory import DriverFactory
from utilities.generate_allure_report.generate_complete_execution_report import AllureReport
from utilities.logger import customLogger
from utilities.move_to_archive import MoveToArchiveFolder

driver = None
_LOG = customLogger(logging.INFO)
environment = None


@pytest.fixture(scope='class')
def class_level_setup(request, get_param):
    print("NARESH NARESH NARESH NARESH NARESH NARESH NARESH NARESH NARESH NARESH NARESH NARESH")
    """
    This will execute before each class contains test cases
    """
    global driver, _LOG, environment
    _LOG.info("Initializing Driver")
    environment = get_param["env"]
    # Initializing webdriver
    print("driver  ", driver)
    driver_init = DriverFactory()
    driver = driver_init.driver_initialize(get_param["browser"])
    print("driver is now  ", driver)
    login = LoginPageOR(driver, _LOG)

    print("I am login object", login)

    request.cls.login = login
    header = HeaderPage(driver, _LOG)

    print("I am header object", header)

    request.cls.header = header
    #
    _LOG.info("Initializing required classes")
    environment = environment.upper() + "_ENVIRONMENT"

    print("I am environment object", environment)
    print("I am request.cls ", request.cls)

    request.cls.driver = driver
    print("I am request.cls ", request.cls)

    if request.cls is not None:
        # request.cls.driver = driver
        pass
    request.cls.environment = environment
    yield _LOG, environment, login, header
    driver.quit()


@pytest.fixture()
def setup(request):
    print("Suresh Suresh Suresh Suresh Suresh Suresh")

    """
    This will execute before executing test case method
    """
    global driver, _LOG
    # Landing page - Dashboard page
    driver.get("https://www.google.co.in/")
    test_name = request.node.name
    _LOG.info("####### EXECUTING TEST CASE -- '" + test_name + "'")
    yield
    # This will execute after executing test case method
    _LOG.info("Tear down driver")
    test_name = request.node.name
    if request.node.rep_setup.failed:
        _LOG.error("####### TEST CASE '" + test_name + "' IS FAILED")
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            _LOG.error("####### TEST CASE '" + test_name + "' IS FAILED")
            screenshot_path = CaptureScreenShot.capture_screenshot(driver, test_name)
            # attaching screen shot to allure report
            allure.attach.file(screenshot_path, attachment_type=AttachmentType.PNG)
            # below statement will add result to Labmda Test tool
            # driver.execute_script("lambda-status=failed")
        else:
            _LOG.info("####### TEST CASE '" + test_name + "' IS PASSED")
            # below statement will add result to Labmda Test tool
            # driver.execute_script("lambda-status=passed")


def pytest_addoption(parser):
    """
    Parse the command prompt value of browser variable
    """
    parser.addoption("--browser", default='Chrome', help="browsers like Firefox, Chrome or IE")
    parser.addoption("--env", default="stage", help="Select application environment like "
                                                    "staging, production etc")


@pytest.fixture(scope="session")
def get_param(request):
    print("DEV DEV DEV")

    """
    Providing parsed browser value to set up method
    """
    command_param = {"browser": request.config.getoption("--browser"), "env": request.config.getoption("--env")}
    return command_param


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
     execute all other hooks to obtain the report object
    """
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session")
def one_time_setup():
    print("one_time_setup one_time_setup one_time_setup one_time_setup")


    """
    This fixture will execute only once before start execution of all test cases
    """

    paths = GetPath()
    move_to_archive = MoveToArchiveFolder()
    move_to_archive.move_to_archive(paths.archive_report_path(), paths.execution_report_path())
    move_to_archive.move_to_archive(paths.archive_screenshot_path(), paths.screenshot_folder_path())
    paths.screenshot_folder_path()
    paths.execution_report_path()
    paths.log_file_path()
    yield
    _LOG.info("Generating execution report")
    report = AllureReport()
    report.call_allure_report_bat()
    # report.close_allure()

