# 부동산 매물 정보 스크래핑(송파 헬리오시티)

# [출력 결과]
'''===== 매물 {idx} =====
    매매일 : {}
    거래 유형 : {}
    가격 : {} (만원)
    타입 : {}
    층 : {}'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1050')
# User-agent 정보가 HeadlessChrome으로 뜨게하지 않기 위해 추가
options.add_argument('user-agent=Mozilla/5.0 \
                     (Macintosh; Intel Mac OS X 10_15_7) \
                     AppleWebKit/537.36 (KHTML, like Gecko) \
                     Chrome/91.0.4472.114 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://realty.daum.net/home/apt/danjis/20037"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')

colnames = ['계약일', '거래' '거래가격', '타입', '층수']
# print(soup.findAll('div'))
dates = list(map(lambda x: x.get_text(),
             soup.find_all('div',
              attrs={
                  'class':"rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r \
                      rn-deolkf rn-11t4n93 rn-1471scf rn-1wbh5a2 rn-1w6e6rj \
                           rn-143r1dj rn-n6v787 rn-o11vmf rn-ebii48 rn-gul640 \
                               rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw\
                                    rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 \
                                        rn-bauka4 rn-q42fyq rn-qvutc0"})))
trades = list(map(lambda x: x.get_text(),
             soup.find_all('div',
              attrs={
                  'class':"rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r \
                      rn-deolkf rn-11t4n93 rn-1471scf rn-143r1dj rn-o11vmf \
                           rn-ebii48 rn-vw2c0b rn-1mnahxq rn-61z16t rn-p1pxzi \
                               rn-11wrixw rn-wk8lta rn-9aemit rn-1mdbw0j\
                                    rn-gy4na3 rn-bauka4 rn-q42fyq rn-qvutc0"})))
price_type_heights = list(map(lambda x: x.get_text(),
             soup.find_all('div',
              attrs={
                  'class':"rn-1oszu61 rn-1efd50x rn-14skgim rn-rull8r \
                      rn-mm0ijv rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r \
                           rn-deolkf rn-6koalj rn-1mlwlqe rn-eqz5dr rn-1wbh5a2 \
                               rn-1w6e6rj rn-1mnahxq rn-61z16t rn-p1pxzi\
                                    rn-11wrixw rn-ifefl9 rn-bcqeeo rn-wk8lta \
                                        rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bnwqim rn-1lgpqti"})))

prices = price_type_heights[::3]
types = price_type_heights[1::3]
heights = price_type_heights[2::3]

for idx , i in enumerate(zip(dates, trades, prices, types, heights)):
    print(f'''===== 매물 {idx} =====
    매매일 : {i[0]}
    거래 유형 : {i[1]}
    가격 : {i[2]} (만원)
    타입 : {i[3]}
    층 : {i[4]}''')

browser.quit()
'''
===== 매물 0 =====
    매매일 : 21. 7. 2
    거래 유형 : 월세
    가격 : 7억/260 (만원)
    타입 : 113B
    층 : 12
===== 매물 1 =====
    매매일 : 21. 6. 29
    거래 유형 : 전세
    가격 : 3억 5,788 (만원)
    타입 : 84B
    층 : 4
===== 매물 2 =====
    매매일 : 21. 6. 22
    거래 유형 : 월세
    가격 : 9억/220 (만원)
    타입 : 113B
    층 : 22
===== 매물 3 =====
    매매일 : 21. 6. 22
    거래 유형 : 월세
    가격 : 5억/250 (만원)
    타입 : 84A
    층 : 19
===== 매물 4 =====
    매매일 : 21. 6. 22
    거래 유형 : 전세
    가격 : 3억 5,788 (만원)
    타입 : 84A
    층 : 7'''