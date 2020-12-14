import os
import signal
import stat
import subprocess

from selenium_base.path import GetPath
from utilities.generic_functions import GenericFunctions


class AllureReport:
    _pro = None

    def call_allure_report_bat(self):
        global _pro
        path = GetPath()
        report_path = path.execution_report_path()
        report_executable_path = path.allure_report_executable_path()
        if 'window' in GenericFunctions.get_os().casefold():
            report_executable_path = path.allure_report_executable_path()+'\\report.bat'
            _pro=subprocess.Popen([report_executable_path, report_path])
        else:
            report_executable_path = path.allure_report_executable_path() + '/report.bash'
            st = os.stat(report_executable_path)
            os.chmod(report_executable_path, st.st_mode | stat.S_IEXEC)
            subprocess.Popen([report_executable_path, report_path])


    def close_allure(self):
        global _pro
        os.kill(_pro.pid, signal.CTRL_C_EVENT)

    # call_allure_report_bat()

# ar = AllureReport()
# ar.call_allure_report_bat()