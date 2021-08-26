import requests
from bs4 import BeautifulSoup4 as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)



driver = webdriver.Chrome(options=chrome_options)


try:
    driver.get('https://www.naver.com/')

    driver.find_element_by_css_selector('#query').send_keys('삼성전자 배당금')
    driver.find_element_by_id('search_btn').click()
    driver.find_element_by_css_selector('.lst_total._list_base > li a.total_tit').click()
    main_window = driver.current_window_handle
    for win_name in driver.window_handles:
        if main_window != win_name:
            driver.switch_to.window(win_name)
            cafe_main = driver.find_element_by_css_selector('#cafe_main')
            driver.switch_to.frame(cafe_main)
            time.sleep(2)
            from bs4 import BeautifulSoup4 as bs
            page = bs(driver.page_source, 'lxml')


            title = driver.find_element_by_css_selector('.title_text')
            contents = driver.find_elements_by_css_selector('.se-component-content > div > div > p > span')
            content_text = ''
            for content in contents:
                content_text += content.text
            print(title.text)
            print(content_text)



    # driver.find_element_by_css_selector('.id_ittech').click()
    # driver.execute_script("document.querySelectorAll('.id_ittech')[0].click()")

    # for node in driver.find_elements_by_css_selector('div.type_topstory > ul > li'):
    #     print(node.text)


except:
    import traceback
    print(traceback.format_exc())

finally:
    pass
    driver.quit()
