# insert = []
# first = input("입력을 받습니다.") # input은 문자열로 받는다

# insert = first.split()

# a = insert[1:len(insert)-int(insert[0])]
# del insert[0:len(insert)-int(insert[0])]
# for num in a :
#     insert.append(num)


# print(f"수정된 리스트는 {insert}")



# 파일의 형식
# 09:12:23 11:14:35
# 10:34:01 13:23:40
# 10:34:31 11:20:10

inp = input("입력 값").split(":")

file = """
09:12:23 11:14:35
10:34:01 13:23:40
10:34:31 11:20:10
"""
filenew=[]
file = file.split()
for time in file :
    filenew.append(time.split(":"))
    
count=0

for time in range(0,3) :
    if filenew[time*2][0]*10000 + filenew[time*2][1]*100 + filenew[time*2][2] < inp[0]*10000 + inp[1]*100 + inp[2] < filenew[time*2+1][0]*10000 + filenew[time*2+1][1]*100 + filenew[time*2+1][2]:
        count += 1

print(f"그 시간에는 회사에 사람이 {count}명 있었습니다!")




