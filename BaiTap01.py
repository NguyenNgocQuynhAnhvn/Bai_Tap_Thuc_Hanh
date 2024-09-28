from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# khoi tao webdriver
driver = webdriver.Chrome()
# mo trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)
# thoi gian cho 2s
time.sleep(2)
# lay tat ca cac the a
tags = driver.find_elements(By.TAG_NAME, value = "a")
# tao ra danh sach cac lien ket
links = [tag.get_attribute("href") for tag in tags]
# xuat thong tin
for link in links:
    print (link)
# dong webdriver
driver.quit()















