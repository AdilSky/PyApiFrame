# FileName : Excel.py
# Author   : Adil
# DateTime : 2017/12/10 13:08
# SoftWare : PyCharm

import xlrd
import os
from openpyxl.reader.excel import load_workbook

from Wm_Api import readConfig as RC

Rc = RC.ReadConfig()

class Excel(object):
    '''定义一个excel类'''

    def __init__(self):
        '初始化基本信息'

        self.path = Rc.path
        self.excelPath = os.path.join(self.path,'caseData')

    def readExcel(self,excelName,SheetName):
        '读取excel'

        self.excelName = os.path.join(self.excelPath,excelName)

        self.Rb = xlrd.open_workbook(self.excelName)

        self.Rs = self.Rb.sheet_by_name(SheetName)

        # 获取行数
        rows = self.Rs.nrows
        # 定义一个dict存放单条用例
        # self.titleDict = dict.fromkeys(self.Rs.row_values(0))
        # 取第一行的表头存为list。
        self.titleList = self.Rs.row_values(0)
        # 定义一个list 存放 所有用例
        self.caseList = []
        for r in range(1,rows):
            rowValues = self.Rs.row_values(r)
            # print(r)
            # print(self.Rs.row_values(r))
            # self.caseInfo = dict.fromkeys(self.Rs.row_values(0),self.Rs.row_values(r))
            # print(self.caseInfo)
            # 将列表组合成 字典 这是 将列表转换为字典的一个方法。
            self.caseDict = dict(zip(self.titleList,rowValues))
            # 下面是将字典转换为列表，
            # print(list(self.caseDict))
            # print(self.caseDict.values())
            # print(self.caseDict)
            # 将字典再拼接为列表。
            self.caseList.append(self.caseDict)
        # print(self.caseList)
        # 返回caseList
        return self.caseList







if __name__ == '__main__':

    excel = Excel()
    excel.readExcel('ApiInfo.xlsx','Login')