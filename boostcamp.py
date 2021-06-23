import collections

words = "Hello everybody"
counter = collections.Counter(words)

# print(counter)
print(counter.most_common(3)[0][0])

a = [1, 2]
b = a
c = a[:]
a[0] = 30
print(b)

print(counter)
for fr, ba in enumerate(counter):
    print(fr, ba, " ", end='',)
