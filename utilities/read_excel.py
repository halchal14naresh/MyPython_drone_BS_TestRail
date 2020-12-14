import xlrd

from selenium_base.path import GetPath

work_book = None
sheet = None


def get_sheet(excel_path: str, sheet_name: str) -> None:
    """
    Open the excel file from the given excel_path.
    Get sheet from given sheet name
    """
    global work_book, sheet
    work_book = xlrd.open_workbook(excel_path)
    sheet = work_book.sheet_by_name(sheet_name)


def get_data(excel_path: str, sheet_name: str) -> list:
    """
    Return list of row test_data for given sheet
    """
    global work_book, sheet
    get_sheet(excel_path, sheet_name)
    rows = sheet.nrows
    excel_data_list = []
    for row in range(1, rows):
        excel_data_list.append(sheet.row_values(row))
    return excel_data_list

def get_testcaseid(testcase: str) -> list:
    global work_book, sheet
    getpath = GetPath()
    get_sheet(getpath.testrail_mapping_path("testrail_mapping.xls"), "Sheet1")
    rows = sheet.nrows
    cols = sheet.ncols
    excel_data_list = []
    for row in range(1, rows):
        if (sheet.cell_value(row, 0) == testcase):
            for col in range(1, cols):
                if ("" != sheet.cell_value(row, col)):
                    excel_data_list.append(int(sheet.cell_value(row, col)))
    return excel_data_list
