from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)



driver = webdriver.Chrome(options=chrome_options)


try:
    driver.get('https://auto.naver.com/car/mainList.nhn')


    # driver.find_element_by_css_selector('.id_ittech').click()
    # firstEmblem = driver.execute_script("document.querySelectorAll('.emblem')[0]")
    firstEmblem = driver.find_elements_by_css_selector('div.emblem > ul > li > a')[0]
    brand = firstEmblem.find_element_by_css_selector('span').text
    
    firstEmblem.click()
    time.sleep(1.5)
    modelList = driver.find_elements_by_css_selector('#modelListArea > ul > li >div.model_ct > div > a.model_name')
    for i in range(len(modelList)):
        modelList = driver.find_elements_by_css_selector('#modelListArea > ul > li >div.model_ct > div > a.model_name')
        carName = modelList[i].find_element_by_css_selector('span > strong').text
        modelList[i].click()
        time.sleep(1.5)
        driver.find_element_by_css_selector('.tab_mnu > ul > li.data > a').click()
        firstModelName = driver.find_elements_by_css_selector('.lineup_top div .col_contents > div.col')[0]
        modelName = firstModelName.find_element_by_css_selector('.price_section > dl >dt').text
        firstMainInfo = driver.find_elements_by_css_selector('.lineup_btm_td > .main_info > ul')[0]
        mainInfo = ''
        for info in firstMainInfo.find_elements_by_css_selector('li'):
            mainInfo += info.text + '/ '
        print(f'브랜드: {brand}, 차종: {carName}, 모델명: {modelName}, 주요제원: {mainInfo}')
        driver.back()
        time.sleep(1.5)
        driver.back()
        time.sleep(1.5)



    # firstModel = driver.find_elements_by_css_selector('#modelListArea > ul > li > a')

except:
    import traceback
    print(traceback.format_exc())

finally:
    driver.quit()