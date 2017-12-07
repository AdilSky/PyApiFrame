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
        ssl._create_default_https_context = ssl._create_unverified_context
        url = "https://www.yiyao.cc/user/loginWeb"
        values = {'username':'xzyc001','password':'111111'}
        # values['username'] = 'xzyc001'
        # values['password'] = '111111'
        # 临时解决https的问题
        response = requests.post(url, values, verify=True)
        self.result = response.json()
        self.assertEqual(self.result['success'],True)
        self.assertEqual(self.result['error'],None)
        self.assertEqual(self.result['message'],'登录成功')

    def test_unvalid_user_login(self):
        '''用户不存在'''
        ssl._create_default_https_context = ssl._create_unverified_context
        url = "https://www.yiyao.cc/user/loginWeb"
        values = {'username':'xzyc221','password':'111111'}
        # values['username'] = 'xzyc001'
        # values['password'] = '111111'
        # 临时解决https的问题
        response = requests.post(url, values, verify=True)
        self.result = response.json()
        self.assertEqual(self.result['success'],False)
        self.assertEqual(self.result['error'],'100040')
        self.assertEqual(self.result['message'],'用户不存在')

    def test_unvalid_password_login(self):
        '''密码错误'''
        ssl._create_default_https_context = ssl._create_unverified_context
        url = "https://www.yiyao.cc/user/loginWeb"
        values = {'username':'xzyc001','password':'222222'}
        # values['username'] = 'xzyc001'
        # values['password'] = '111111'
        # 临时解决https的问题
        response = requests.post(url, values, verify=True)
        self.result = response.json()
        self.assertEqual(self.result['success'],False)
        self.assertEqual(self.result['error'],'100008')
        self.assertEqual(self.result['message'],'用户名密码错误')

    def test_unvalid_name_password_login(self):
        '''密码错误'''
        ssl._create_default_https_context = ssl._create_unverified_context
        url = "https://www.yiyao.cc/user/loginWeb"
        values = {'username': '', 'password': ''}
        # values['username'] = 'xzyc001'
        # values['password'] = '111111'
        # 临时解决https的问题
        response = requests.post(url, values, verify=True)
        self.result = response.json()
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['error'], '100001')
        self.assertEqual(self.result['message'], '用户名为空')


if __name__ == '__main__':

    unittest.main()


