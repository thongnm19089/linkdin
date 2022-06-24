# from lib2to3.pgen2 import driver
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# url = 'https://www.facebook.com/login'
# driver.get(url)

# #login
# taikhoan = '0965431900'
# User =  driver.find_element_by_id('email')
# User.send_keys(taikhoan)

# password = 'Thong01bg'
# Pass =  driver.find_element_by_id('pass')
# Pass.send_keys(password)

# Pass.send_keys(Keys.ENTER)

# password = 'Thong01bg'
# Pass =  driver.find_element_by_class_name('kvgmc6g5 oygrvhab')
# Pass.send_keys(password)
# Pass.send_keys(Keys.ENTER)
# sleep(5)
# driver.close()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
#login
driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
url = 'https://www.facebook.com/'
driver.get(url)

taikhoan = '0968800341'
User =  driver.find_element_by_id('email')
User.send_keys(taikhoan)

password = 'Thong01bg'
Pass =  driver.find_element_by_id('pass')
Pass.send_keys(password)

Pass.send_keys(Keys.ENTER)

while True:
 time.sleep(7)
 ten = 'yeuemmm'
 seach = driver.find_element_by_css_selector('.notranslate')
 seach.send_keys(ten)
 seach.send_keys(Keys.ENTER)