# FileName : login_v1_test.py
# Author   : Adil
# DateTime : 2017/12/10 13:26
# SoftWare : PyCharm

# 从excel读取数据

import unittest,requests

from  Wm_Api.common import Excel


Ex = Excel.Excel()

class LoginTest(unittest.TestCase):
    '''定义登录类'''

    def setUp(self):
        self.base_url = 'https://www.yiyao.cc'


    def tearDown(self):
        pass


    def testLogin(self):
        '''用户登录'''
        try:
            caseList = Ex.readExcel('ApiInfo.xlsx','Login')

            for caseDict in caseList:
                url = self.base_url + caseDict['ApiLoad']
                method = caseDict['Method']
                caseData = caseDict['CaseData']
                caseRun = caseDict['CaseRun']
                caseName = caseDict['CaseName']
                expectValue = caseDict['ExpectValue']
                caseData = eval(caseData)
                expectValue = eval(expectValue)
                if caseRun == 'Y':
                    if method == 'Post':

                        print(caseName)
                        response = requests.post(url, caseData)
                        self.result = response.json()
                        self.assertEqual(self.result['success'],expectValue['success'],msg=None)
                        self.assertEqual(self.result['error'],expectValue['error'],msg=None)
                        self.assertEqual(self.result['message'],expectValue['message'],msg=None)
                        print(self.result)

                    if method == 'Get':
                        pass
        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)


if __name__ == '__main__':

    unittest.main()