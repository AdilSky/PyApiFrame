# FileName : runTest.py
# Author   : Adil
# DateTime : 2017/12/7 21:07
# SoftWare : PyCharm

import unittest,os,time
from Wm_Api.common.HTMLTestRunner import HTMLTestRunner

from Wm_Api.common.EMail import  Email

from Wm_Api import readConfig as RC


class ExecutCase(object):
    '''定义执行用例的类'''

    def __init__(self):
        '''初始化参数'''
        readConfig = RC.ReadConfig()
        self.Msg_Title = readConfig.getMail('Msg_Title')
        self.casePath = os.path.join(RC.rootPath, 'test_case')
        self.reportPath = os.path.join(RC.rootPath, 'test_report')
        self.Text_description = readConfig.getMail('Text_description')

    def exeCase(self):
        '''执行用例'''
        test_discover = unittest.defaultTestLoader.discover(self.casePath, pattern='*test.py')
        now = time.strftime("%Y-%m-%d-%H_%M_%S")
        filename = self.reportPath + r'\result-' + now + '.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title=self.Msg_Title, description=self.Text_description)
        runner.run(test_discover)
        fp.close()
        self.sendEmail(filename)

    def sendEmail(self,filename):

        if self.on_off == 'on':
            sendMail = Email()
            mail = sendMail.sendEMail(filename)
            if mail:
                print("发送成功！")
            else:
                print("发送失败！")
        else:
            print ('邮件未发送，如需发送邮件，请打开邮件发送开关！')


