__all__ = [] #여기 들어있는거만 import 가능하다.

"""

모듈이나 package는 사용하는 파일과 똑같은 경로에 있거나
라이브러리에 있어야 한다.

"""

import collections

def longestPalindrome(s: str) -> str:
        # 2,3칸이 오른쪽으로 이동한다.
    def expand(left:int, right:int):
        while left >=0 and right<=len(s)-1 and s[left] == s[right]:
            #2개가 같으면 옆으로 한칸씩 확장해서 비교
            left -= 1
            right += 1
        return s[left+1:right]
    if len(s) < 2 or s[:] == s[::-1]:
        return s
    result = ''
    for i in range(0, len(s)-1): # range도 a이상 b미만 이구나... 
        result = max(result, expand(i,i+1), expand(i, i+2), key = len) # 바로바로 최댓값만 저장. 왜 i+2는 9임에도 s[right]에 8이 들어가 오류가 나지 않는 걸까?
        print(s[i:i+2], i+2)
    return result

# 브루트 포스 방법 
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(0,len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return f"{i}{j}"

# class Solution:
#     def twoSum( nums: list[int], target: int) -> list[int]:
#         for i, n in enumerate(nums):
#             compliment = target - n

#             if compliment in nums[i+1:]:
#                 print( nums.index(n), i, nums[i+1:].index(compliment) + (i+1) )


class Solution:
    def twoSum( nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return 
            num_map[num] = i
            


            
nums = [2,7,11,15]
target = 9

#Solution.twoSum(nums,target)

d = {0:1, 4:2}
if 0 in d:
    print(d)
if 2 in d:
    print("Adw")




height = [0,1,0,2,1,0,1,3,2,1,2,1]

# 투 포인터를 이용한 풀이
class Solution:
    def trap(height: list[int]) -> int:
        left, right = 0,len(height)-1
        left_max, right_max = 0,0
        gathered_rain = 0

        while left<right:
            left_max = max(left_max, height[left]) # 자동으로 수정해주니까 뺀 값은 항상 고인 물의 양이 된다. 최고 높이에 이를때 까지.
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                gathered_rain += left_max - height[left]
                left += 1

            if right_max < left_max:
                gathered_rain += right_max - height[right]
                right -= 1
        
        print( gathered_rain )

                            
# 스택을 이용한 풀이
class Solution:
    def trap(height: list[int]) -> int:
        stack = []
        gathered_rain = 0

        for i in range(len(height)):
            #변곡점을 만나는 경우. 여기서 변곡점은 이전 값보다 지금 값이 더 큰경우를 의미
            while stack and height[i] > height[stack[-1]]: # -1은 최댓값( len(stack)-1 )을 의미한다. 따라서 가장 최근에 넣은 값. 하지만 pop으로 빠져나가는 경우가 있다는걸 고려해야한다.
                #스택에서 꺼낸다.   
                top = stack.pop() # 바로 이전 i가 top에 할당된다.
                print("top :", top)

                if not len(stack): # stack이 비어있다면
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1
                print(f"dis : {distance}")
                waters = min(height[i], height[stack[-1]]) - height[top]
                print("water :", waters)
                gathered_rain += distance*waters

            stack.append(i)
            print(stack)
        return gathered_rain
                
def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        if len(nums) < 3:
            return result
        
        red = collections.defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                red[0-(i+j)] = i,j
                
            if i in red:
                red[i].append(i)
                result.append(red[i])
        
        print(red[i])

nums = [-1,0,1,2,-1,-4]
threeSum(nums)

        


Solution.trap(height)

