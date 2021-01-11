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

# 데크 자료형을 이용한 최적화
def is_palindrome_bydeque(pa:str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()
    for char in pa:
        if char.isalnum():
            strs.append(char)
    # 팰린드롬 여부 판별
    while(len(pa) > 1):
        if pa.popleft() != pa.pop():
            return False
    return True
