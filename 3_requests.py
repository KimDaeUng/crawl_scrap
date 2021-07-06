import requests
# 항상 이렇게 쌍으로 쓴다.
# 1. 페이지 요청해 받아오기
res = requests.get('http://google.com')
# 2. 문제가 생기면 오류를 내뱉고 종료
res.raise_for_status()
# print('Response code :', res.status_code) # 200 is normal

# Check 
# if res.status_code == requests.codes.ok:
#     print("It's normal")
# else:
#     print("There're some problem. [error code ", res.status_code, "]")

print(len(res.text)) 
print(res.text)
# 3. 파일로 저장
with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)