from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/quynh/OneDrive/Tài liệu/GitHub/project02/geckodriver.exe"

# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options = options, service=ser)

# Tạo url
url = 'https://pythonscraping.com/pages/files/form.html'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 1 giây
time.sleep(1)

firstname_input = driver.find_element(By.XPATH, "//input[@name='firstname']")
lastname_input = driver.find_element(By.XPATH, "//input[@name='lastname']")

firstname_input.send_keys('Ngoc Quynh Anh')
time.sleep(1)
lastname_input.send_keys('Nguyen')
time.sleep(1)
button = driver.find_element(By.XPATH, "//input[@type ='submit']")
button.click()
time.sleep(3)
driver.quit()










