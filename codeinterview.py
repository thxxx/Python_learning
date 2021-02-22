palin = "A man, a plan, a canal:Panama"
notpalin = "race a car"

# 리스트를 이용하는 방법
def is_palindrome( pa:str ) -> bool:
    newpa = []
    # 영소문자, 숫자만 남긴다
    for char in pa:
        if char.isalnum():
            newpa.append(char.lower())
    # 팰린드롬 여부 판별
    while( 1 < len(newpa)):
        if newpa.pop(0) != newpa.pop():
            return False
    return True

import re

# # 데크 자료형을 이용한 최적화
# def is_palindrome_bydeque(pa:str) -> bool:
#     # 자료형 데크로 선언
#     strs: Deque = collections.deque()
#     for char in pa:
#         if char.isalnum():
#             strs.append(char)
#     # 팰린드롬 여부 판별
#     while(len(pa) > 1):
#         if pa.popleft() != pa.pop():
#             return False
#     return True

# 슬라이싱을 이용한 문제 풀이
def is_palindrome_byslice(pa:str) -> bool:
    pa = pa.lower()
    # 정규식으로 불필요한 문자 필터링
    pa = re.sub('[^a-z0-9]', '', pa) #re는 import해야한다. re.sub 기능 알아두기
    #re.sub는 pa의 정규식표현 부분[1]을 [2]로 바꿔준다.
    return pa == pa[::-1] # 뒤집는다는 뜻

print(is_palindrome(palin))
print(is_palindrome_byslice(palin))
print(is_palindrome(notpalin))
print(is_palindrome_byslice(notpalin))

# 문제2. 문자열 뒤집기
rever = ["h","l","o"]

def reversee(listt: list[str]) -> None:
    listt.reverse()
    # 변수를 하나 더 안만드로 두개 위치 바꾸기
    left, right = 0, len(listt)-1
    while(right>left):
        listt[left], listt[right] = listt[right], listt[left] # , 를 이용해서 바로 위치 바꾸는 기술
        left += 1
        right -= 1

logs = ["digit1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

digits, letters = [], []
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log) # 숫자, 문자 따로 구분부터
    else :
        letters.append(log)

letters.sort() # 이렇게 하면 그냥 앞에서부터 정렬( 식별자를 구분하지 않는다. )
letters.sort(key = lambda x:(x.split()[1:], x.split()[0])) # [1:] 로 정렬하고, 같으면 후순위 [0]
# x를 공백으로 나눈 것의 1번째 index부터 끝까지 라는 뜻. 리스트를 굳이 하나 더 만들지 않고 바로 사용했다..
print(letters + digits)

# 657. Robot to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        n = 0
        key = "UDLR"
        for move in moves:
            if move == "U":
                y += 1
            if move == "D":
                y -= 1
            if move == "L":
                x -= 1
            if move == "R":
                x += 1
        return x==0 and y==0


# 베스트 대답. 생각도 못했다. 내장함수 활용의 중요성
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("R")==moves.count("L") and moves.count("U")==moves.count("D")
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s) # str은 
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] not in vowels:
                left +=1
                continue
                
            elif s[right] not in vowels:
                right -=1
                continue
            else:
                s[left],s[right] = s[right],s[left] # str은 할당을 지원하지 않는다.
                left +=1
                right -=1
        return "".join(s) # list인 s를 str로 출력해준다 


a = Solution()
print(a.reverseVowels("hello"))

# 람다를 아용한 로그파일 재정렬

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit()==True: # 식별자를 제외하고 숫자인이 문자인지 파악
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0])) #람다식 활용.
        return letters + digits

import collections

dict_ = collections.OrderedDict()
dict_["wed"] = 1
dict_["sec"] = 3
dict_["dw"] = 2

print(dict_)