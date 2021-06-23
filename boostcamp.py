
import functools
a = [1, 2, 3, 4, 5]
b = ''.join(str(e) for e in a)  # 이거 보다는
c = ''.join(map(str, a))  # 가 낫다.

print(int(b)-5000)


f = (functools.reduce(lambda x, y: 10 * x + y, [1, 2, 3, 4, 5], 0))
print(type(f))

# 1 Two sums
nums = [1, 2, 3]
for i, v in enumerate(nums):
    print(f"i:{i}, v:{v}")

for p, s in enumerate(nums[1:]):
    print(p, s)
dict = {}
for i, v in enumerate(nums):
    dict[v] = i

print(dict)
