# FileName : comPrice_test.py
# Author   : Adil
# DateTime : 2017/12/12 15:15
# SoftWare : PyCharm

import unittest,requests

from  Wm_Api.common import Excel
import json

Ex = Excel.Excel()

class ComPriceTest(unittest.TestCase):
    '''定义比价类'''

    def setUp(self):
        self.com_url = 'http://bijia.yiyao.cc'
    def tearDown(self):
        pass
    def testComPrice(self):
        '''比价神器'''
        print('比价神器', '\n')
        resultList = []
        titleList = []
        try:
            caseList = Ex.readExcel('ApiInfo.xlsx','ComPrice')
            for caseDict in caseList:
                # print("****")
                # print(caseDict)
                # # 打印 字典keys转化为 list
                # print(list(caseDict))
                # titleList = list(caseDict)
                # # 打印 字典values 转化为list
                # print(list(caseDict.values()))
                # print("****")
                url = self.com_url + caseDict['ApiLoad']
                method = caseDict['Method']
                caseData = caseDict['CaseData']
                caseRun = caseDict['CaseRun']
                caseName = caseDict['CaseName']
                expectValue = caseDict['ExpectValue']
                caseData = eval(caseData)
                headers = {'content-type': 'application/json; charset=utf8'}
                if caseRun == 'Y':
                    if method == 'Post':
                        print(caseName)
                        keyValue=['感冒']
                        #keyValue.append(caseData(['keyword']))
                        print(keyValue)
                        expectValue = eval(expectValue)
                        caseData = json.dumps(caseData)
                        response = requests.post(url, caseData,headers=headers)
                        self.result = response.json()
                        reCode = self.assertEqual(self.result['code'], expectValue['code'], msg=None)
                        reHint = self.assertEqual(self.result['hint'], expectValue['hint'], msg=None)
                        if reCode is None and reHint is None:
                            caseDict['CaseResult'] = 'Pass'
                        else:
                            caseDict['CaseResult'] = 'Fail'
                        print('返回结果', end=': ')
                        print(self.result, '\n')
                        # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                        caseDict['ResultInfo'] = str(self.result)
                    else:
                        print('返回结果: 用例设置无需执行，故没有执行！', '\n')
                    resultList.append(caseDict)
                    # print(resultList)

        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)
        finally:
            Ex.writeExcel('ComPrice', titleList, resultList)

if __name__ == '__main__':

    unittest.main()