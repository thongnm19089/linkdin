from curses import window
from lib2to3.pgen2 import driver
from pydoc import pager
from re import I
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

#login


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
driver.get('https://www.google.com/')


timkiem = input("\n nhập từ khóa tìm kiếm : ")
search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.send_keys(timkiem)
search.send_keys(Keys.ENTER)



#lấy link
def GetURL():   
    time.sleep(8)
    page_source = BeautifulSoup(driver.page_source, "html.parser")
# print(page_source)
    profiles = page_source.find_all("a", class_ = "sVXRqc")

    all_profile_url = []
    for profile in profiles:
        ID = profile.get('href')
        # URL = "https://www.linkedin.com" + ID
        if ID not in all_profile_url:
            all_profile_url.append(ID)

# a = "\n"   
# print(a.join(all_profile_url))
# print(GetURL())


    time.sleep(8)
    # page_source = BeautifulSoup(driver.page_source, "html.parser")
# print(page_source)
    profiles2 = page_source.find_all("div", class_ = "yuRUbf")

    all_profile_urls = []
    for profile2 in profiles2:
        href = profile2.find("a")['href']
        if href not in all_profile_urls:
            all_profile_urls.append(href)
    return all_profile_urls + all_profile_url

# a = "\n"   
# print(a.join(all_profile_url))
# print(GetURL())


#số trang muốn lấy

URL_all = []

try:
    while True:
        URLs_one_page = GetURL()
        sleep(2)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(2)
        next_botton= driver.find_element(By.ID,'pnnext')
        next_botton.click()
        URL_all = URL_all + URLs_one_page
except: 
    SST = 0
    with open (timkiem + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['STT', 'link post']
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()
        for colour in URL_all:
            SST +=1
            thewriter.writerow({'STT':SST, 'link post': colour})
    a = "\n"   
    print(a.join(URL_all))
    sleep(5)
    driver.close()

#     sleep(10) 
#     print('số trang đã hết')
# f = open('linkdin.csv', 'w')
# writer = csv.writer(f)
# writer.writerow(URL_all)
# f.close()

# SST = 0
# with open (timkiem + '.csv', 'w', newline='') as csvfile:
#     fieldnames = ['STT', 'link post']
#     thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     thewriter.writeheader()
#     for colour in URL_all:
#         SST +=1
#         thewriter.writerow({'STT':SST, 'link post': colour})


# a = "\n"   
# print(a.join(URL_all))
# sleep(5)
# driver.close()