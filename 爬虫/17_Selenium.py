# coding:utf-8
from selenium import webdriver

driver = webdriver.PhantomJS()

# 打开百度，只有在完全打开的情况下才会继续执行后面的程序
driver.get("https://www.baidu.com/")



from selenium.webdriver.common.keys import Keys

# 获取id = "kw"的标签值
element = driver.find_element_by_id("kw")

# 在id = "kw"的标签输入"美女"
driver.find_element_by_id("kw").send_keys(u"美女")

# 点击id = "su"的标签
driver.find_element_by_class_name("btn self-btn bg s_btn").click()

# 获取网页源码
driver.page_source()

# 截取打开页面的图片
driver.save_screenshot("baidu.png")