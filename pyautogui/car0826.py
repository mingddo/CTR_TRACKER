
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup4 as bs


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)



driver = webdriver.Chrome(options=chrome_options)


try:
    driver.get('https://auto.naver.com/car/mainList.nhn?importYn=N')
    # driver.find_element_by_css_selector('.id_ittech').click()
    # driver.execute_script("document.querySelectorAll('.id_ittech')[0].click()")
    # for node in driver.find_elements_by_css_selector('div.type_topstory > ul > li'):
    #     print(node.text)
    page = bs(driver.page_source, 'lxml')
    driver.find_element_by_css_selector('.tx.kr > a').click()
    makers = [node.text.strip() for node in page.select('#_vendor_select_layer > .ly_maker_lst > .maker_group > .emblem_area > ul > li')]
    print(makers)


except:
    import traceback
    print(traceback.format_exc())

finally:
    driver.quit()
