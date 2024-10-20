from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd
import getpass
from selenium.webdriver import ActionChains

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/quynh/OneDrive/Tài liệu/GitHub/project02/geckodriver.exe"

# Khởi tạo đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox hiển thị giao diện (headless = False)
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options=options, service=ser)

# Tạo url
url = 'https://www.facebook.com/'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 1 giây
time.sleep(1)

# nhập thông tin người dùng
my_number = input('Please provide your phone number: ')
my_password = getpass.getpass('Please provide your password: ')
actionchains = ActionChains(driver)
# Login

# Tìm phần tử input username và password
username_input = driver.find_element(By.XPATH, "//input[@type='text']")
password_input = driver.find_element(By.XPATH, "//input[@type='password']")

# Nhập thông tin và nhấn nút Enter
username_input.send_keys(my_number)
password_input.send_keys(my_password)
password_input.send_keys(Keys.ENTER)

# Chờ để đăng nhập hoàn tất
time.sleep(5)  # Chờ trang đăng nhập chuyển đổi

# Bắt đầu tạo bài đăng
post_box = driver.find_element(By.XPATH, "//span[text()=' bạn đang nghĩ gì thế?']")
post_box.click()

# Chờ cho phần cửa sổ bài đăng mở ra
time.sleep(3)  # Chờ một chút để cửa sổ mở ra

# Tìm phần tử để nhập nội dung bài đăng
post_input = driver.find_element(By.XPATH,"//span[text()=' bạn đang nghĩ gì thế?']" )
post_input.send_keys("This is an automated post from Selenium!")  # Nội dung bài đăng

# Chờ 2 giây để kiểm tra lại nội dung
time.sleep(30)

# Tìm và nhấn nút Đăng (Post)
post_button = driver.find_element(By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']")
post_button.click()

# Chờ 5 giây để hoàn tất
time.sleep(5)

# Đóng trình duyệt
driver.quit()