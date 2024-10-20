from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# khoi tao webdriver
driver = webdriver.Chrome()
url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
driver.get(url)
time.sleep(3)

# ul_tags = driver.find_elements(By.TAG_NAME, "ul")
# print(ul_tags)

# for index, value in enumerate(ul_tags):
#     print(f"Index: {index}, Value:{value.text}")

# ham in ra tat ca cac nhac si bat dau bang 'List of'
elements = driver.find_elements(By.XPATH, "//a[starts-with(text(), 'List of')]")
links = [element.get_attribute('href') for element in elements]

# In ra các liên kết tìm được
print("Các liên kết liên quan đến các nhạc sĩ bắt đầu bằng 'List of':")
for link in links:
    print(link) 
d = pd.DataFrame({"Name": [], "Year active": []})
# Truy cập vào link đầu tiên bắt đầu bằng chữ "A"
# Truy cập liên kết đầu tiên
driver.get(links[0])

# Chờ trang tải
time.sleep(2)
# Tìm tất cả các hàng chứa thông tin về ban nhạc và thời gian hoạt động
tags_ul = driver.find_elements(By.TAG_NAME, "ul")
tags_li = tags_ul[24] .find_elements(By.TAG_NAME, "li")

links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href")for tag in tags_li]
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title")for tag in tags_li]

for link in links:
    driver.get(link)
    #print(link)
    "Lay ten"
    try:
        # Name_element = driver.find_element(By.XPATH, "//h1[span[text()]]")
        Name_element = driver.find_element(By.XPATH, "//h1[@id='firstHeading']//span[@class='mw-page-title-main']")
        Name = Name_element.text
    except:
        ""

    "Lay ngay hoat dong"
    try:
        Year_active_element = driver.find_element(By.XPATH,"""//th[span[contains(text(), 'Years active')]]/following-sibling::td""")
        # Year_active_element = driver.find_element(By.XPATH, "//td[contains(text(), '1965–1969, 1973, 1984, 2015')]")
        YearActive = Year_active_element.text
    except:
        ""

    "Tao dictionary thong tin nhac si"
   
    musician_dict = {"Name": Name, "Year active": YearActive}
    musician_df = pd.DataFrame([musician_dict])
    # print(musician_df)

    "Them thong tin vao dataframe"
    d = pd.concat([d, musician_df], ignore_index=True)
print(d)

# determining the name of the file
file_name = 'Musicians2.xlsx'

# saving the Excel
d.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')

time.sleep(3)

driver.quit()
























