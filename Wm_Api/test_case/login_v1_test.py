# FileName : login_v1_test.py
# Author   : Adil
# DateTime : 2017/12/10 13:26
# SoftWare : PyCharm

# 从excel读取数据

import unittest,requests

from  Wm_Api.common import Excel
import json

Ex = Excel.Excel()

class LoginTest(unittest.TestCase):
    '''定义登录类'''

    def setUp(self):
        self.base_url = 'https://www.yiyao.cc'
        caseList = Ex.readExcel('ApiInfo.xlsx', 'Login')

        for caseDict in caseList:
            print(caseDict)

    def tearDown(self):
        print(self.result)


    def loginTest(self):
        '''用户登录'''

        caseList = Ex.readExcel('ApiInfo.xlsx','Login')
        self.base_url = 'https://www.yiyao.cc'
        for caseDict in caseList:
            # print(caseDict)

            url1 = self.base_url + caseDict['ApiLoad']
            method = caseDict['Method']
            caseData = caseDict['CaseData']
            caseRun = caseDict['CaseRun']
            print(url1)
            if caseRun == 'Y':
                if method == 'Post':
                    print(caseDict['CaseName'])
                    print(caseData)
                    print(type(caseData))
                    caseData = eval(caseData)
                    print(type(caseData))
                    # 下面是上面三条打印的结果，看似一样，但是类型不一样。所以需要转为dict
                    # {'username': 'xzyc001', 'password': '111111'}
                    # < class 'str'>
                    #
                    # < class 'dict'>

                    dataList = list(caseData)
                    print(dataList)
                    # caseData = json.dumps(caseData)
                    url = "https://www.yiyao.cc/user/loginWeb"
                    values ={'username': 'xzyc001', 'password': '111111'}
                    print(type(values))
                    values = caseData
                    # values = json.dumps(values)
                    print(values)
                    response = requests.post(url1, caseDict['CaseData'])
                    self.result = response.json()
                    self.assertEqual(self.result['success'],True,msg=None)
                    self.assertEqual(self.result['error'],None,msg=None)
                    self.assertEqual(self.result['message'],'登录成功',msg=None)
                    print(self.result)
                if method == 'Get':

                    pass


        # try:
        #     url = self.base_url +
        #     values = {'username':'xzyc001','password':'111111'}
        #     # values['username'] = 'xzyc001'
        #     # values['password'] = '111111'
        #     # 临时解决https的问题
        #     response = requests.post(url, values)
        #     self.result = response.json()
        #     self.assertEqual(self.result['success'],True,msg=None)
        #     self.assertEqual(self.result['error'],None,msg=None)
        #     self.assertEqual(self.result['message'],'登录成功',msg=None)
        # except BaseException as msg:
        #     self.assertIsNone(msg,msg=None)
        #     print(msg)




        pass




if __name__ == '__main__':

    loginTest = LoginTest()
    loginTest.loginTest()