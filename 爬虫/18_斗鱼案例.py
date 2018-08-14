# coding:utf-8
import unittest
from selenium import webdriver
# 用来使用操作鼠标、键盘、标签
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

class douyu(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.num = 0
        self.count = 0

    # 测试方法必须以test开头
    def testDouYu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            soup = bs(self.driver.page_source, "lxml")
            # 查房间名,返回列表
            names = soup.find_all("h3",{"class":"ellipsis"})
            # 查观众人数
            numbers = soup.find_all("span",{"class":"dy-num fr"})

            # zip方法，把列表合并成元组:[(1,a),(2,b),(3,c)...]
            for name,number in zip(names,numbers):
                print(u"房间名:%s" %name.get_text().strip(),u"\t观众人数:%s" %numbers.get_text().strip())
                self.num += 1
            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break
            self.driver.find_element_by_class_name("shark-pager-next").click()

    # 测试结束执行的方法
    def tearDown(self):
        # 退出PhantomJS()浏览器
        print("当前网站直播人数" + str(self.num))
        print("当前网站观众人数" + str(self.count))
        self.driver.quit()

if __name__ == '__main__':
    # 启动测试模块
    unittest.main()

# driver.get("https://www.douyu.com/directory/all")

# 输入用户名密码
# driver.find_element_by_name("form_email").send_keys("username")
# driver.find_element_by_name("form_password").send_keys("password")

# 点击登陆
# driver.find_element_by_class_name("bn-submit").click()

# if driver.page_source.find("shark-pager-disable-next") != -1:  # 没到最后一页

