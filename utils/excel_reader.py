# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/4 14:59  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import xlrd

class ExcelOperation:
    def __init__(self, path):
        self.path = path
        self.excel = xlrd.open_workbook(path)

    def get_sheet(self, sheet_name):
        sheet = self.excel.sheet_by_name(sheet_name)
        return sheet
