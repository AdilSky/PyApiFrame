# FileName : login_test.py
# Author   : Adil
# DateTime : 2017/12/6 21:44
# SoftWare : PyCharm

import unittest
import requests
import ssl
class LoginTest(unittest.TestCase):
    '''用户登录'''

    def setUp(self):
        self.base_url = 'https://www.yiyao.cc/user/loginweb'

    def tearDown(self):
        print(self.result)


    def test_valid_user_login(self):
        '''有效用户登录'''
        print('有效用户登录')
        try:
            url = "https://www.yiyao.cc/user/loginWeb"
            values = {'username':'xzyc001','password':'111111'}
            # values['username'] = 'xzyc001'
            # values['password'] = '111111'
            # 临时解决https的问题
            response = requests.post(url, values)
            self.result = response.json()
            self.assertEqual(self.result['success'],True,msg=None)
            self.assertEqual(self.result['error'],None,msg=None)
            self.assertEqual(self.result['message'],'登录成功',msg=None)
        except BaseException as msg:
            self.assertIsNone(msg,msg=None)
            print(msg)

        #print(self.result)

    def test_unvalid_user_login(self):
        '''用户不存在'''
        print('用户不存在')
        try:
            url = "https://www.yiyao.cc/user/loginWeb"
            values = {'username':'xzyc221','password':'111111'}
            # values['username'] = 'xzyc001'
            # values['password'] = '111111'
            # 临时解决https的问题
            response = requests.post(url, values)
            self.result = response.json()
            self.assertEqual(self.result['success'],False,msg=None)
            self.assertEqual(self.result['error'],'100040',msg=None)
            self.assertEqual(self.result['message'],'用户不存在',msg=None)
        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)

    def test_unvalid_password_login(self):
        '''密码错误'''
        print('密码错误')
        try:
            url = "https://www.yiyao.cc/user/loginWeb"
            values = {'username':'xzyc001','password':'222222'}
            # values['username'] = 'xzyc001'
            # values['password'] = '111111'
            # 临时解决https的问题
            response = requests.post(url, values)
            self.result = response.json()
            self.assertEqual(self.result['success'],False,msg=None)
            self.assertEqual(self.result['error'],'100008',msg=None)
            self.assertEqual(self.result['message'],'用户名密码错误',msg=None)
        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)

    def test_unvalid_name_password_login(self):
        '''用户密码为空'''
        print('用户名密码为空')
        try:

            url = "https://www.yiyao.cc/user/loginWeb"
            values = {'username': '', 'password': ''}
            # values['username'] = 'xzyc001'
            # values['password'] = '111111'
            # 临时解决https的问题
            response = requests.post(url, values)
            self.result = response.json()
            self.assertEqual(self.result['success'], False,msg=None)
            self.assertEqual(self.result['error'], '100001',msg=None)
            self.assertEqual(self.result['message'], '用户名为空',msg=None)
        except BaseException as msg:
            self.assertIsNone(msg, msg=None)
            print(msg)

if __name__ == '__main__':

    unittest.main()


