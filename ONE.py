import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
# print(driver.current_url)
URL = 'https://www.one-line.com/en'
driver.get(url=URL)
print(driver.current_url)
driver.implicitly_wait(0.5)

# 자동화 크롬으로 열기 위에는 디버깅 크롬으로 열기 (쿠키 때문에 이렇게 함.)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(options=options)

# ONE 크롤링
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver(options=options)
### 추가된 부분 오류 해결
# chromedriver = 'chromedriver.exe'
# driver = webdriver.Chrome(chromedriver)

element = driver.find_element_by_name('ctrack-field')
element.send_keys('SELB37758700')
submitBtn = driver.find_element_by_id('trackform')
submitBtn.find_element_by_class_name('btn-small').submit()


driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
table = driver.find_element_by_class_name('ui-jqgrid-btable')
tbody = table.find_element_by_tag_name('tbody')
rows = tbody.find_elements_by_tag_name("tr")
body = rows[0].find_elements_by_tag_name("td")[3]
# ctr = body.find_element_by_tag_name('a')
print(body.text)

# for index, value in enumerate(rows):
#     body=value.find_elements_by_tag_name("td")[2]
#     print(body.text)
#     break
# ctrNo.click()
# 여기까지가 BL 번호 치고 조회
# BL번호는 ONE의 경우 ONEY를 떼고 조회해야지 나옴.
# 찾아야 할 부분 찾아서 for 문으로 돌리고 해당하는 정보 엑셀 저장. 