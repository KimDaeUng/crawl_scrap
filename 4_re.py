import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave ...
# caae, cabe, ...

p = re.compile("ca.e")
# . : single character > e.g. (ca.e): care, cafe, case (O) | caffe (X)
# ^ : begins with      > e.g. (^de) : desk, destinvation (O) | fade (X)
# $ : ends with        > e.g. (se$) : case, base (O) | face (X)

def print_match(m):
    # print when it matches
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string)   # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 인덱스
        print("m.end():", m.end())     # 일치하는 문자열의 끝 인덱스
        print("m.span():", m.span())     # 일치하는 문자열의 시작 / 끝 인덱스

    else:
        print("not matched")

# match : check if given character is mathced with pattern from leftmost
# print not matched
# m = p.match("good care")
# print_match(m)
# print matched chracter
# m = p.match("careless")
# print_match(m)


# search : 주어진 문자열 중에 일치하는 것이 있는지 확인
# m = p.search('good care')
# print_match(m)

# m = p.search('careless')
# print_match(m)

# findall : 일치하는 모든 것을 리스트 형태로 반환
lst = p.findall('good care cafe')
print(lst)

# 정규식 사용법 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열"): 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열"): 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미  > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작      > desk, destination (O) | fade (X)
# $ (se$)  : 문자열의 끝       > case, base (O) | face (X)

# 추가 자료: w3school python part 예제, python re documentation

