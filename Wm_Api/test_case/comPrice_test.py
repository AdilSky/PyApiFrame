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
                        self.assertEqual(self.result['code'],expectValue['code'],msg=None)
                        self.assertEqual(self.result['hint'],expectValue['hint'],msg=None)
                        #self.assertIn( ['感冒咳嗽颗粒', '感冒安片'],keyValue,msg=None)
                        #self.assertEqual(self.result['message'],expectValue['message'],msg=None)
                        print(self.result)
        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)

if __name__ == '__main__':

    unittest.main()