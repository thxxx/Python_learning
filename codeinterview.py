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

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split() 
                    if word not in banned]
                # 안띄우면 스페이스도 없애버리는구나
        # 이러면 words 에는 banned를 제외한 단어들만 저장된다.
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

# leetcode 의 가장 빠른 방법
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
		
		# convert to lower case and split string into words by spaces and punctuation
        a = re.split(r'\W+', paragraph.lower())
		
		# make new list consisitng of words not in banned list (remove banned words)
        b = [w for w in a if w not in banned]
		
		# return value that counted max times in the new list
        return max(b, key = b.count)

# 그룹 애너그램

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs :
            result = ''.join(sorted(word)) # sorted 를 쓰면 요소를 다 분리해서 정렬된 list로 만든다. 
            # 이걸 다시 join으로 합쳐주면 같은 아나그램 단어들은 같은 key의 value가 된다.
            anagrams[result].append(word) #append로 하나의 key에 여러 value가 할당될 수 있도록한다.
        return anagrams.values()
        

# 가장 긴 팰린드롬 부분 문자열

s = ["21","132","2323"]

print(max(s, key=len) )

class Solution:
    def oddEvenList(self, head: listNode) -> listNode:
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head.next or not head or left == right :
            return head
        root = start = ListNode(None)
        root.next = head
        
        # start, end 부터 일단 지정 for은 0에서 시작하는거 제발 기억하자
        for i in range(left - 1):
            start = start.next
        end = start.next

        
        for i in range(right - left):
            prev, start.next = start.next, end.next
            end.next.next, end.next = prev, end.next.next

        return root.next

        class Node:
	def __init__(self, item, next):
		self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None # 마지막노드. 가장 최근에 들어온 노드를 가리킨다.
    
    def push(self, item):
        self.last = Node(item, self.last) # 새롭게 부여된 self.last의 next가 이전 self.last가 된다.

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item # 없어진 노드의 값을 반환


import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(lists: list[ListNode]) -> ListNode:
        root = result = ListNode(None) # 이건 루트와 리절트를 각각 따로 하는것과는 다르다. root 는 result가 된다.
        heap = []

        #각 연결리스트의 루트를 힙에 저장
        """
        for li in lists:
            heapq.heappush(heap, (li.val, li))
        """
        # 근데 이렇게 하면 같은 값을 가지고 있는게 있을때 heappop에서 뭘 뽑을지 에러가 난다. 따라서 그 다음의 우선순위를 지정해주기
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
        while heap:
            pop = heapq.heappop(heap)
            result.next = pop[2]
            index = pop[1]

            heapq.heappush(heap, (result.next.val, index, result.next))

        return root.next

