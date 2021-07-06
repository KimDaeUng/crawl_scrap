import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all('li', attrs={'class': re.compile("^search-product")})

for item in items:
    name = item.find('div', attrs={'class':"name"}).get_text()
    price = item.find('strong', attrs={'class' : 'price-value'}).get_text()
    rate = item.find('em', attrs={'class':'rating'}).get_text()
    rate_cnt = item.find('span', attrs={'class':'rating-total-count'}).get_text()
    print(name, price, rate, rate_cnt)