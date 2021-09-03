import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from openpyxl import Workbook


def get_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_data(page):
    '''
    엑셀에 저장
	* export.xlsx 와 동일하게 생성
    '''
    nodes = page.select('#detail > tbody > tr')
    wb = Workbook()
    ws = wb.active
    header = []
    for head in page.select('#detail > thead > tr > th'):
        header.append(head.text)
    ws.append(header)
    
    # tbody 저장
    for node in nodes:
        tempData = node.select('td')
        tempList = []
        for d in tempData:
            tempList.append(d.text.strip())
        ws.append(tempList)

    wb.save('One.xlsx')


    


def controll_page(driver, container_no):
    target = driver.find_element_by_css_selector('#ByContainer > div > div > div > textarea')

    action = ActionChains(driver)
    action.move_to_element(target)

    action.move_to_element(target).perform()

    target.click()
    target.clear()
    target.send_keys(container_no)
    ###############여기까지 했다아
    #################
    driver.find_element_by_css_selector('#btnSearch').click()
    time.sleep(2)
    driver.execute_script(f"var a = document.querySelectorAll('td > a');for (var i=0; i<a.length;i++){{ if (a[i].innerText==='{container_no}') {{a[i].click();break;}}}}")


if __name__ == '__main__':
    '''
    Container : TCNU4277832, B/L : ONEYSELB95846900
    Container : TEMU7180609, B/L : ONEYSELB65271501
    '''
    container_no = '#'
    url = 'https://www.wsl.com/Tracking/Public'

    driver = get_webdriver()
    try:
        driver.get(url)
        controll_page(driver, container_no)  # 화면 컨트롤 작성

        page = bs(driver.page_source, 'lxml')

        get_data(page)  # 데이터 추출후 프린트

    finally:
        # driver.quit()
        pass

    import sys

    sys.exit(0)
