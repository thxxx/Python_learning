
s = [3,1,2,3,4,2,1,]
for index, char in enumerate(s):
    print(char)

import collections
print(collections.Counter(s).most_common(2))