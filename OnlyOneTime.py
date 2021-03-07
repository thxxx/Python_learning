# import random

# TRIAL = 100000
# same = 0
# for _ in range(TRIAL):
#     birthdays = []
#     for i in range(23):
#         birthday = random.randint(1,365)
#         if birthday in birthdays:
#             same += 1
#             break
#         birthdays.append(birthday)

# print(f"{(same/TRIAL * 100)} %")

stones = "aaWSDfadswef"
jewels = "ws"
print(sum(map(stones.count, jewels)))

def numJewelsInStones(self, jewels: str, stones: str) -> int:
    return sum([s in jewels for s in stones])
        
