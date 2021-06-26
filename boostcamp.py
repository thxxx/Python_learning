
import functools
a = [1, 2, 3, 4, 5]
b = ''.join(str(e) for e in a)  # 이거 보다는
c = ''.join(map(str, a))  # 가 낫다.

print(int(b)-5000)


f = (functools.reduce(lambda x, y: 10 * x + y, [1, 2, 3, 4, 5], 0))
print(type(f))

# 1 Two sums
"""
nums = [1, 2, 3]
for i, v in enumerate(nums):
    print(f"i:{i}, v:{v}")

for p, s in enumerate(nums[1:]):
    print(p, s)
dict = {}
for i, v in enumerate(nums):
    dict[v] = i

print(dict)
for p in nums:
    dict[target-p]
    
#1-1 dict 사용
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()
        s=0
        
        for i,n in enumerate(nums):
            if (target-n) in pair:
                return [pair[target-n], i]
            else:
                pair[n] = i
    
"""
# 1-2 직접 in으로
nums = [3, 4, 5, 1]
print(nums[0:])


def trap(height: list) -> int:
    left, right = 0, 0
    l, r = 0, len(height)-1

    result = 0

    while(l <= r):
        if left < right:
            if left > height[l]:
                result += left-height[l]
                print(f"{result}, {l}")
            else:
                left = height[l]
            print("height l ", height[l])
            l += 1
        else:
            if right > height[r]:
                result += right-height[r]
                print(f"{result}, {r}")
            else:
                right = height[r]
            print("height r ", height[r])
            r -= 1

    return result


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

height.sort()

print(height)

print(height[::2])

pl = [1] * len(nums)
pr = [1] * len(nums)

print(f"pl : {pl}")
print(f"pr : {pr}")

# 편법없이 투포인터 느낌

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        pl = [1] * len(nums)
        pr = [1] * len(nums)
        prev = 1
        for i in range(1, len(nums)):
            prev = nums[i-1]
            pl[i] = prev * pl[i-1]
        prev = 1
        for i in range(len(nums)-2, -1, -1):
            prev = nums[i+1]
            pr[i] = prev * pr[i+1]

        return [pl[i]*pr[i] for i in range(len(nums))]

"""
print(sorted(nums)[::-1])
print(nums)

# 시간 복잡도를 고려한 풀이

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        if sorted(prices)[::-1] == prices:
            return 0
        prev = sys.maxsize
        for p in prices:
            result = max(result, p - prev)
            prev = min(p,prev)

            
            
            
        return result
"""

print(pow(10, 2))
answer = []
s = ['/a/a/a_v1.z', '/a/b/c_v2.e', '/d/v/c/a_v4.d', '/d/v/c/a_v3.d']
dic = {}
for d in s:
    while '/' in d:
        i = d.index('/')
        d = d[i+1:]
    temp = [d[0], ".", d[-1]]
    temp = ''.join(temp)
    if temp in dic:
        dic[temp] += 1
    else:
        dic[temp] = 1
for k in dic:
    if dic[k] > 1:
        answer.append(k)
print(answer)

s = [1, 2, 3]
print(len(s))

param0 = ["INT", "INT", "BOOL", "SHORT", "LONG"]

answer = []
types = {
    'BOOL': 1,
    'INT': 2,
    'SHORT': 4,
    'INT': 8,
    'LONG': 16
}
prev = ""

for pa in param0:
    if pa == 'LONG':
        if len(answer) % 8 > 0:
            answer.append('.' * (8 - len(answer) % 8))
        answer.append('#'*8)
        answer.append('#'*8)
    else:
        if pa == 'BOOL' and prev == 'BOOL' and len(answer) % 8 != 0:
            answer.append('.')
        if len(answer) % 8 + types[pa] > 8:
            answer.append('.'*(8-len(answer) % 8))

        answer.append('#' * types[pa])
        print(f"{pa} , {len(answer) % 8}")
    prev = pa

print(''.join(answer))


dw = []
dw.append('d'*5)
print("Dsfwe ", len(dw))
