import collections

def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        result_set = set(result)
        if len(nums) < 3:
            return result
        
        red = collections.defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                red[0-(nums[i]+nums[j])] = [nums[i],nums[j]]
                
            if nums[i] in red:
                red[nums[i]].append(nums[i])
                result.append(red[nums[i]])

        for a in result:
            a.sort()
            a = tuple(a)
            result_set.add(a)

        print(list(result_set))

nums = [-1,0,1,2,-1,-4]
threeSum(nums)

#문제집의 풀이
"""
정렬부터 한다. 하지만 정렬의 시간복잡도도 존재.
기준으로 삼는 i의 값이 중복이 되는 값인 경우 건너뛴다.
1. 브루트 포스. 포인터를 3개를 두고 다 더하는걸 고려한다.
2. 투 포인터. 하나의 i를 잡고 투포인터로 계산한다.
"""

def productExceptSelf(nums: list[int]) -> list[int]:
    out = []
    p = 1

    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    
    for i in range(len(nums)-1, 0-1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out

nums = [1,2,3,4]
print(productExceptSelf(nums))


def add_to_dict(dicti: dict, addkey:str, defi:str):
  if type(dicti) != dict():
    print("You need to send a dictionary. You sent: ", type(dicti))
asw = {}
add_to_dict(asw,"Dwqd","Awd")



prices = [3,7,2,7,1,5,3,4]

class Solution:
    def maxProfit(prices: list[int]) -> int:
        profit = 0
        min_num = min(prices)

        # keep update max and min
        for p in prices:
            min_num = min(min_num,p)
            profit = max(profit, p - min_num)

        return profit


print(Solution.maxProfit(prices))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome( head: ListNode) -> bool:
        reverse = None
        fast = slow = head

        if not fast or not fast.next:
            return True

        # 런너를 이용하여 역순 연결리스트(reverse에) 만든다.
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        
        if fast:
            slow = slow.next
        
        # 역순 연결리스트의 팰린드롬 여부 판별
        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next

        # 계속 같아서 reverse의 값이 None이 될때까지 수행되면 된거임.        
        return not reverse


