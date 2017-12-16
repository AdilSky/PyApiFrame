# FileName : WmApi_test.py
# Author   : Adil
# DateTime : 2017/12/13 19:41
# SoftWare : PyCharm

import unittest,requests

import os,json
from Wm_Api.common import Excel
from Wm_Api import readConfig as RC


class WmApiTest(unittest.TestCase):
    '''未名Api测试'''

    @classmethod
    def setUpClass(cls):
        cls.yiyaoURL = 'https://www.yiyao.cc'
        cls.bijiaURL =  'http://bijia.yiyao.cc'
        # 实例化 Ex
        cls.Ex = Excel.Excel()

    @classmethod
    def tearDownClass(cls):

        pass


    def testComPrice(self):
        '''比价神器'''
        print('比价神器', '\n')

        resultList = []
        titleList = []
        caseList = self.Ex.readExcel('ApiInfo.xlsx', 'ComPrice')
        for caseDict in caseList:
            url = self.bijiaURL + caseDict['ApiLoad']
            titleList = list(caseDict)
            caseNum = caseDict['CaseNum']
            method = caseDict['Method']
            caseData = caseDict['CaseData']   # 这样获取的数据 是str 类型的
            caseDataDict = eval(caseData)              # 使用eval 转换为dict 类型
            # 将dict类型转化为json类型
            data = json.dumps(caseDataDict)
            caseRun = caseDict['CaseRun']
            caseName = caseDict['CaseName']
            # 设置请求头
            headers = {'content-type': 'application/json; charset=utf8'}
            # 设置报告打印内容
            print('用例 ' + caseNum, end=': ')
            print(caseName)
            print('数据参数 : ' + caseData)
            print('搜索商品 : ' + caseDataDict['keyword'])
            if caseRun == 'Y':
                expectValue = eval(caseDict['ExpectValue'])
                if method == 'Post':
                    response = requests.post(url, data, headers=headers)
                    result = response.json()
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['hint'] == expectValue['hint']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result, '\n')
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)

                if method == 'Get':
                    response = requests.get(url, params=data, headers=headers)
                    result = response.json()
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['hint'] == expectValue['hint']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result, '\n')
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)
            else:
                print('返回结果: 用例设置无需执行，故没有执行！', '\n')
            resultList.append(caseDict)
            # print(resultList)
        self.Ex.writeExcel('ComPrice', titleList, resultList)

    def testLogin(self):
        '''用户登录'''
        print('用户登录', '\n')
        resultList = []
        titleList = []
        caseList = self.Ex.readExcel('ApiInfo.xlsx', 'Login')
        for caseDict in caseList:
            url = self.yiyaoURL + caseDict['ApiLoad']
            titleList = list(caseDict)
            caseNum = caseDict['CaseNum']
            method = caseDict['Method']
            caseData = caseDict['CaseData']   # 这样获取的数据 是str 类型的
            data = eval(caseData)              # 使用eval 转换为dict 类型
            caseRun = caseDict['CaseRun']
            caseName = caseDict['CaseName']

            # 设置请求头
            # headers = {'content-type': 'application/json; charset=utf8'}
            # 设置报告打印内容
            print('用例 ' + caseNum, end=': ')
            print(caseName)
            print('数据参数 : ' + caseData)

            if caseRun == 'Y':
                expectValue = eval(caseDict['ExpectValue'])
                if method == 'Post':
                    response = requests.post(url, data)
                    result = response.json()
                    # 设置断言
                    if result['success'] == expectValue['success'] and result['error'] == expectValue['error']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result, '\n')
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)

                if method == 'Get':
                    response = requests.get(url, params=data)
                    result = response.json()
                    # 设置断言
                    if result['success'] == expectValue['success'] and result['error'] == expectValue['error']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result, '\n')
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)
            else:
                print('返回结果: 用例设置无需执行，故没有执行！', '\n')
            resultList.append(caseDict)
            # print(resultList)
        self.Ex.writeExcel('Login', titleList, resultList)

if __name__ == '__main__':
    unittest.main()





