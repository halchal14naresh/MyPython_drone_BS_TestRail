from utilities.read_config import ReadConfig
from utilities.read_excel import get_testcaseid


class Class1:
    def method1(self,testcase):
        print("asdadasdas")
        #return get_testcaseid(testcase)
        readProp = ReadConfig()
        print("TestRail Url =", readProp.get_property_value('TestRail', "testrail_url"))
        print("TestRail Url =", readProp.get_property_value('TestRail', "testrail_pass"))



obj = Class1()
aaa  = obj.method1("one_data")

# for row in range(len(aaa)):
#     print(aaa[row])


