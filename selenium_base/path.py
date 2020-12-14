import os.path

from utilities.generic_functions import GenericFunctions


class GetPath:

    def log_file_path(self, doc="this returns the path till logs folder"):
        """
        this returns the path till logs folder
        """
        try:
            log_path = os.path.join("logs")
            GenericFunctions.isdir_present(log_path)
            return log_path
        except Exception as e:
            print("Error in log_file_path" + str(e))

    def screenshot_folder_path(self, doc="this returns the path till screenshot folder"):
        """
        this returns the path till screenshot folder
        """
        try:

            screenshot_path = os.path.join("resources","screenshots")
            GenericFunctions.isdir_present(screenshot_path)
            return screenshot_path
        except Exception as e:
            print("Error in screenshot_folder_path" + str(e))

    def test_data_path(self, excel_name:str, doc="this returns the path of test_data folder. "
                                                 "It contains test test_data files"):
        """
        this returns the path of given data file from test_data folder.
        'test_data' folder contains test multiple test_data files
        """
        try:

            data_file = os.path.join("resources","test_data",excel_name)
            return data_file
        except Exception as e:
            print("Error in data file path" + str(e))

    def config_path(self, doc="this returns the path of config.ini file"):
        """
        this returns the path of config.ini file
        """
        try:
            conf_path = os.path.join("config","config.ini")
            return conf_path
        except Exception as e:
            print("Error in config.properties path" + str(e))

    def execution_report_path(self, doc="this returns the path of execution report folder"):
        """
        This returns the path of execution report
        """
        try:
            report_path = os.path.join("target","execution_report")
            GenericFunctions.isdir_present(report_path)
            return report_path
        except Exception as e:
            print("Error in execution report path" + str(e))

    def allure_report_executable_path(self, doc="this returns the path of allure report executable batch or bash file"):
        """
        This returns the path of path where allure report .bat or .bash file is present
        """
        try:
            allure_report_path = os.path.join("utilities","generate_allure_report")
            return allure_report_path
        except Exception as e:
            print("Error in allure report path" + str(e))

    def archive_report_path(self, doc="this returns the path of archive folder"):
        """
        This returns the path of execution report
        """
        try:
            archive_path = os.path.join("target","archive")
            GenericFunctions.isdir_present(archive_path)
            return archive_path
        except Exception as e:
            print("Error in execution report path" + str(e))

    def archive_screenshot_path(self, doc="this returns the path of archive folder"):
        """
        This returns the path of execution report
        """
        try:
            archive_path = os.path.join("resources","archive")
            GenericFunctions.isdir_present(archive_path)
            return archive_path
        except Exception as e:
            print("Error in execution report path" + str(e))

    def testrail_mapping_path(self, excel_name: str, doc="this returns the path of test_data folder. "
                                                  "It contains test test_data files"):
        """
        this returns the path of given data file from test_data folder.
        'test_data' folder contains test multiple test_data files
        """
        try:

            data_file = os.path.join("resources", "test_data", excel_name)
            return data_file
        except Exception as e:
            print("Error in data file path" + str(e))