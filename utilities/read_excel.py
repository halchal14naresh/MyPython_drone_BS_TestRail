import xlrd

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
