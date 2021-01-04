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
from utilities.klov_reports import Reports
from utilities.logger import customLogger
from utilities.move_to_archive import MoveToArchiveFolder
from utilities.read_config import ReadConfig
from utilities.read_excel import get_testcaseid
from utilities.testrail import APIClient

driver = None
_LOG = customLogger(logging.INFO)
environment = None
report = None
klov_server = None


def init_report():
    read_prop = ReadConfig()
    projectName = read_prop.get_property_value("REPORT", "projectName")
    reportName = read_prop.get_property_value("REPORT", "reportName")
    mongoDbHost = read_prop.get_property_value("REPORT", "mongoDbHost")
    mongoDbPort = int(read_prop.get_property_value("REPORT", "mongoDbPort"))
    klovServerAddress = read_prop.get_property_value("REPORT", "klovServerAddress")
    return Reports(projectName, reportName, mongoDbHost, mongoDbPort, klovServerAddress)


report = init_report()


@pytest.fixture(scope='class')
def class_level_setup(request, get_param):
    """
    This will execute before each class contains test cases
    """
    global driver, _LOG, environment
    _LOG.info("Initializing Driver")
    environment = get_param["env"]
    # Initializing webdriver
    driver_init = DriverFactory()
    driver = driver_init.driver_initialize(get_param["browser"])
    login = LoginPageOR(driver, _LOG)
    request.cls.login = login
    header = HeaderPage(driver, _LOG)
    request.cls.header = header
    #
    _LOG.info("Initializing required classes")
    environment = environment.upper() + "_ENVIRONMENT"
    request.cls.driver = driver
    if request.cls is not None:
        # request.cls.driver = driver
        pass
    request.cls.environment = environment
    request.cls.report = report
    yield _LOG, environment, login, header, report
    driver.quit()


@pytest.fixture()
def setup(request, get_param):
    """
    This will execute before executing test case method
    """
    global driver, _LOG, report
    runID = get_param["runid"]
    readProp = ReadConfig()
    # Landing page - Dashboard page
    driver.get("https://www.google.co.in/")
    test_name = request.node.name
    report.init_extent_test(test_name)
    report.info_log("####### EXECUTING TEST CASE -- '" + test_name + "'")
    _LOG.info("####### EXECUTING TEST CASE -- '" + test_name + "'")
    yield report
    # This will execute after executing test case method
    _LOG.info("Tear down driver")
    test_name = request.node.name
    case_ids = get_testcaseid(test_name)
    client = APIClient(readProp.get_property_value('TestRail', "testrail_url"))
    client.user = readProp.get_property_value('TestRail', "testrail_user")
    client.password = readProp.get_property_value('TestRail', "testrail_pass")
    success_msg = "This is working fine marked Passed By Selenium Thanks"
    fail_msg = "This is not working fine marked Failed By Selenium Thanks"
    if request.node.rep_setup.failed:
        _LOG.error("####### TEST CASE '" + test_name + "' IS FAILED")
        client.updatetestRail(runID,case_ids,5,fail_msg)
        report.error_log("####### TEST CASE '" + test_name + "' IS FAILED")
        screenshot_path = CaptureScreenShot.capture_screenshot(driver, test_name)
        # below statement will add result to Labmda Test tool
        # driver.execute_script("lambda-status=failed")
        report.info_log("Screenshot: " + screenshot_path)
        report.testcase_result("fail", 'FAILED', screenshot_path)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            _LOG.error("####### TEST CASE '" + test_name + "' IS FAILED")
            client.updatetestRail(runID, case_ids, 5, fail_msg)
            screenshot_path = CaptureScreenShot.capture_screenshot(driver, test_name)
            # attaching screen shot to allure report
            allure.attach.file(screenshot_path, attachment_type=AttachmentType.PNG)
            # below statement will add result to Labmda Test tool
            # driver.execute_script("lambda-status=failed")
            report.error_log("####### TEST CASE '" + test_name + "' IS FAILED")
            screenshot_path = CaptureScreenShot.capture_screenshot(driver, test_name)
            # below statement will add result to Labmda Test tool
            # driver.execute_script("lambda-status=failed")
            report.info_log("Screenshot: " + screenshot_path)
            report.testcase_result("fail", 'FAILED', screenshot_path)

        else:
            _LOG.info("####### TEST CASE '" + test_name + "' IS PASSED")
            client.updatetestRail(runID, case_ids, 1, success_msg)
            # below statement will add result to Labmda Test tool
            # driver.execute_script("lambda-status=passed")
            report.testcase_result("pass", None, None)
            report.info_log("####### TEST CASE '" + test_name + "' IS PASSED")


def pytest_addoption(parser):
    """
    Parse the command prompt value of browser variable
    """
    parser.addoption("--browser", default='Chrome', help="browsers like Firefox, Chrome or IE")
    parser.addoption("--env", default="stage", help="Select application environment like "                                                   "staging, production etc")
    parser.addoption("--runid", default=1, help="this is run id from testrun")


@pytest.fixture(scope="session")
def get_param(request):
    """
    Providing parsed browser value to set up method
    """
    command_param = {"browser": request.config.getoption("--browser"), "env": request.config.getoption("--env") ,"runid": request.config.getoption("--runid")}
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
    # _LOG.info("Generating execution report")
    # report = AreReport()
    # report.call_allure_report_bat()
    # report.close_allure()
    report.flush_report()

