from curses import window
from lib2to3.pgen2 import driver
from pydoc import pager
from time import sleep
from xml.dom.minidom import Document
from attr import s
from numpy import e, number
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.chrome.options import Options
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
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
driver.get(url)

#login
time.sleep(3)
# taikhoan = 'contact@tagon.ai'
taikhoan = 'thongnm.nde19089@vtc.edu.vn'

User =  driver.find_element_by_id('username')
User.send_keys(taikhoan)

time.sleep(3)
# password = '@!(tisd%Fvc5hKt'
password = 'Anhthong01bg'
Pass =  driver.find_element_by_id('password')
Pass.send_keys(password)
Pass.send_keys(Keys.ENTER)

#search
# try:
timkiem = input("\n nhập từ khóa tìm kiếm : ")
search = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
search.send_keys(timkiem)
search.send_keys(Keys.ENTER)
# except:
    
#     search = driver.find_element(By.CSS_SELECTOR, '#global-nav-search > div > button > li-icon > svg > path')
    
#     search.send_keys('python developer jobs')
#     search.send_keys(Keys.ENTER)


#lấy link
def GetURL():   
    time.sleep(8)
    page_source = BeautifulSoup(driver.page_source, "html.parser")
# print(page_source)
    profiles = page_source.find_all("a", class_ = "app-aware-link scale-down")

    all_profile_url = []
    for profile in profiles:
        ID = profile.get('href')
        # URL = "https://www.linkedin.com" + ID
        if ID not in all_profile_url:
            all_profile_url.append(ID)
    return all_profile_url

# a = "\n"   
# print(a.join(all_profile_url))
# print(GetURL())

#số trang muốn lấy

URL_all = []
number_page = int(input("\n nhập số trang muốn lấy  : "))
# try:
for page in range(number_page): 
    URLs_one_page = GetURL()
    sleep(2)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(2)
    next_botton= driver.find_element(By.CLASS_NAME,'artdeco-pagination__button--next')
    next_botton.click()
    URL_all = URL_all + URLs_one_page
# except:
#     sleep(10)
#     print('số trang đã hết')
# f = open('linkdin.csv', 'w')
# writer = csv.writer(f)
# writer.writerow(URL_all)
# f.close()

SST = 0
with open (timkiem + '.csv', 'w', newline='') as csvfile:
    fieldnames = ['STT', 'link post']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()
    for colour in URL_all:
        SST +=1
        thewriter.writerow({'STT':SST, 'link post': colour})
# a = "\n"   
# print(a.join(URL_all))
sleep(5)
driver.close()