import requests
from bs4 import BeautifulSoup
url = 'https://comic.naver.com/webtoon/weekday.nhn'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())

# page에 대해 잘 알고 있을 때
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성 정보 출력
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력

# 잘 모른다면
# print(soup.find('a', attrs={'class':"Nbtn_upload"})) # class="Nbtn_upload"인 a element를 찾아줘
# print(soup.find(attrs={'class':"Nbtn_upload"})) # class="Nbtn_upload"인 어떤 element를 찾아줘

# soup 객체도 XPath 처럼 경로를 다룰 수 있다.
# print(soup.find('li', attrs={'class':'rank01'}))
# rank1 = soup.find('li', attrs={'class':'rank01'})
# print(rank1.a.get_text())
# print(rank1.parent)

# sibling 다음 항목으로 넘어가기
# print(rank1.next_sibling) # 개행 문자가 존재해 아무것도 보이지 않음
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# 위에처럼 두 번 쓰기 불편하다면, next_sibling으로 가되 조건 안에 있는 것만 활용
# 다음 형제 중 'li' 태그인 것만 찾아라
# rank2 = rank1.find_next_sibling('li')
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())

# sibling 이전 항목으로 넘어가기
# rank2 = rank3.previous_sibling.previous_sibling
# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())

# 한 번에 모든 정보를 찾은 다음에 처리하고 싶은 경우
# print(rank1.find_next_siblings('li'))

# attribute가 아닌 text에 대해서도 해당하는 태그 가져올 수 있다.
webtoon = soup.find('a', text='여신강림-164화')
print(webtoon)