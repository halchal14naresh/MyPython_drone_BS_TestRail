import jpype
from jpype import JPackage


# from selenium_base.path import GetPath


class Reports:
    classpath = None
    reports = None

    def __init__(self, projectName, reportName, mongoDbHost, mongoDbPort, klovServerAddress):
        # paths = GetPath()
        # self.classpath = "D:\\Learning\\Python\\SeleniumPythonBaseFramework\\" \
        #                  "JavaFiles\\ExtentReport-jar-with-dependencies.jar"
        # self.classpath = paths.extentreport_jar_path()

        #self.classpath = "F:/EclipseWorkSpace/ext.jar"




        self.classpath = "F:/EclipseWorkSpace/TestProject/target/TestProject-0.0.1-SNAPSHOT-jar-with-dependencies.jar"
        jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', "-Djava.class.path=" + self.classpath)
        print("Step 1 *******")
        jpype.java.lang.System.out.println("hello world")
        extent_report = JPackage('com').reports
        print("Step 2 *******", extent_report, type(extent_report))
        #print(jpype.isThreadAttachedToJVM())
        #jpype.attachThreadToJVM()
        #print(jpype.isThreadAttachedToJVM())
        self.reports = extent_report.ExtentReportFunctions(projectName, reportName, mongoDbHost, mongoDbPort,
                                                           klovServerAddress)
        print("Step 3 *******")
        self.reports.initExtentReport()

        print("Step 4 *******")







    def add_system_info(self, os, env, user):
        self.reports.systemInfo(os, env, user)

    def flush_report(self):
        self.reports.flushReport()

    def info_log(self, infolog):
        self.reports.info(infolog)

    def error_log(self, errorlog):
        self.reports.error(errorlog)

    def init_extent_test(self, test_name):
        self.reports.initExtentTest(test_name)

    def testcase_result(self, testResult, failedReason, screenshotPath):
        self.reports.testcaseResult(testResult, failedReason, screenshotPath)

    def shutdown_JVM(self):
        jpype.shutdownJVM()
