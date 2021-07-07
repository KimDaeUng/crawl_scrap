from bs4.element import ProcessingInstruction
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 해상도 세로 높이 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1050)")
# browser.execute_script("window.scrollTo(0, 2100)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장 
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')
# 새로 로딩한 영화부터는 클래스 이름이 바뀌어 둘 모두를 포함하게 함
# movies = soup.find_all("div", attrs={'class' : ["ImZGtf mpg5gc", "Vpfmgd"]})
# 첫번째 클래스명은 기본값, 새 값 로딩 후에 값이 두 번 중복됌
movies = soup.find_all("div", attrs={'class' : "Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find('div', attrs={'class':'WsMG1c nnK0zc'}).get_text()
    # print(title)

    # 할인 전 가격
    original_price = movie.find("span", attrs={'class':"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(' <할인 되지 않은 영화 제외>')
        continue
    
    # 할인 된 가격
    price = movie.find('span', attrs={"class" : "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 가져오기
    link = movie.find('a', attrs={'class' : "JC71ub"})['href']
    # 올바른 링크: https://play.google.com + link

    print(f'제목 : {title}')
    print(f'할인 전 금액 : {original_price}')
    print(f'할인 후 금액 : {price}')
    print(f'링크 : ', "https://play.google.com" + link)
    print('-' * 100)

browser.quit()