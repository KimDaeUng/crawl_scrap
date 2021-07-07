import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://flight.naver.com/flights/'
browser.get(url) # Url로 이동
time.sleep(2)

# 가는 날 선택 클릭
browser.find_element_by_link_text('가는날 선택').click()

# 이번달 27,28일 선택
# browser.find_elements_by_link_text('27')[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text('28')[0].click() # [0] -> 이번달

# 이번달 27, 다음달 28일 선택
browser.find_elements_by_link_text('27')[0].click() # [0] -> 이번달
browser.find_elements_by_link_text('28')[1].click() # [0] -> 이번달

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# Browser의 웹 페이지에서 특정 element가 나올때까지 대기, 최대 10초
# 성공했을 때 동작 수행
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
finally:
    browser.quit()