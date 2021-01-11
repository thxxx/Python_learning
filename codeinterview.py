palin = "A man, a plan, a canal:Panama"
notpalin = "race a car"

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
    