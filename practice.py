
# pylint:프로그래밍상에서 잘못된 부분을 미리 알려주는거

from math import *  # math안의 모든걸 import하겠다.
import pickle
import sys
from random import *
자료형
print(5)
print('풍선')
print("ㅋ"*9)
print(not 5 > 10)

변수
animal = "강아지"
name = "토리"
age = 4
is_adult = age >= 3
print("우리집" + animal + "는 " + name + "에요")
# print( str(age) + "살 이구요, 어른일까요? " + str(is_adult))
print(age, "살 이구요, 어른일까요? ", is_adult)
# ,엔 빈칸이 생긴다

station = "사당"
print(station, "행 열차가 들어오고 있습니다.")
# File > Preferences > terminal font로 설정
print(1+1)
print(2**3)  # 2의 3승
print(5 % 2)  # 나머지
print(5//3)  # 몫

print(4 <= 6)
print(3 == 3)
print(3+4 == 7)
print(1 != 3)

print((3 > 0) and (3 < 5))  # &
print((3 > 0) or (5 < 3))  # ||

number = 10
print(number)
number += 2
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(type(number))  # 10.0 이 됨

abs(-5)
pow(4, 2)
max(5, 12)
min(1, 3)
round(3.14)
round(3.74)


print(floor(4.99))  # 내림
print(ceil(4.99))  # 올림
print(sqrt(4))  # 제곱근 2.0


print(random())
print(int(43*random()))  # 0~43미만의 값
print(randrange(1, 43))  # 0~43미만의 값 == randint(0,42)

date = int(25*random())+4

sentence = '나는 소년'
print(sentence)
sentence2 = "나는 소년"
print(sentence2)
sentence3 = """
나는 모르겠다
어떻게 해야할지
"""
print(sentence3)

jumin = "980715-1456312"
print("성별 : " + jumin[7])  # 성별 : 1
print("연 :" + jumin[0:2])  # 0이상 2미만 까지 가져옴.
print("일 :" + jumin[4:6])

print("생년월일 :"+jumin[:6])  # 처음부터 6미만까지.
print("뒤 7자리 :"+jumin[7:])  # 7부터 끝까지.
print("뒤 7자리(뒤에서 부터 계산) :"+jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

python = "Python Is Amazing"
print(python.lower())  # 소문자화
print(python.upper())  # 대문자화
print(python[0].isupper())  # 대문자인지 Boolean
print(len(python))  # 문자열길이

print(python.replace("Python", "Java"))  # Python을 Java로 바꿈


index = python.index("n")
print(index)  # 5 출력

index = python.index("n", index + 1)  # 아까찾은 n다음부터 n 검색
print(index)  # 15 출력

print(python.find("Java"))  # 똑같이 찾는거. Java는 없으니까 -1출력
# print(python.index("Java")) #index는 검색 문자열이 없으면 오류.

# 문자열 포맷
# 방법 1
print("나는 %d살 입니다." % 20)  # %d자리에 20 들어감.
print("나는 %s가 좋아요" % "자바")  # 문자열
print("내 학점은 %c 입니다" % "F")  # 한 문자
# %s 는 문자열, 한문자, 숫자 다 상관없다
print("나는 %s 색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아함".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아함".format("파란", "빨간"))  # 앞이 빨간, 뒤가 파란이 된다.
# 방법 3
print("나는 {age}색과 {color}색을 좋아함".format(age=20, color="red"))

# 방법 4 (v3.6이상~)
age = 20
color = "red"
print(f"나는{age}살이고 I like {color}.")  # f를 앞에 붙여서 변수사용

# \n : 줄바꿈
print("나를알고 적을알면 지피지기")
print("나를알고 \"적을알면\" 지피지기")  # 역슬래쉬로 기호들 사용
print("RedApple \rPine")  # \r : 커서를 맨앞으로 이동
print("RedApple\bPine")  # \b : 백스페이스  한 글자 삭제 \t는 탭

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)  # [10,20,30]
subway = ["나", "너", "우리"]
print(subway.index("우리"))

# split도 있다!!!

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")  # append는 맨뒤에 하나 추가.
subway.insert(1, "정형돈")  # 정형돈을 1번째 위치에 추가.

wholeave = subway.pop()  # 제일 뒤에 있는게 빠짐. 빠진사람이 할당

subway.append("나")
print(subway.count("나"))  # 2
# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()  # 1,2,3,4,5로 정렬.
num_list.reverse()  # 5,4,3,2,1로 바뀜.
# num_list.clear()  다 지워짐ㅠㅠ
mix_list = ["조세호", 20, True]  # 자료형에 관계없이 가능

# 리스트 확장
num_list.extend(mix_list)  # 리스트 두개가 합쳐진다

# 사전 만들기!
cabinet = {3: "유재석", 100: "김태호"}  # key, 콜론, value
print(cabinet[3])  # 유재석이 출력.
print(cabinet.get(3))  # 위랑 같다.
# print(cabinet[5]) # KeyError[5]라는 오류 출력 후 바로 프로그램 종료.
print(cabinet.get(5))  # None 이 출력. 종료 안됨.
print(cabinet.get(5, "사용가능"))  # 사용가능 이 출력.

print(3 in cabinet)  # True
print(6 in cabinet)  # Flase

mycabinet = {"A-3": "내꺼", "B-100": "니꺼"}
# 끝에 C-20이라는 Key를 만들고 조세호를 넣는다. C-20이 이미 있으면 값이 업데이트.
mycabinet["C-20"] = "조세호"

# 간 손님
del mycabinet["A-3"]  # A-3키를 삭제
print(mycabinet.keys())  # 키들만 출력
print(mycabinet.values())  # 값들만 출력
print(mycabinet.items())  # 쌍으로 출력. clear로 다 없애기

# 튜플 list와는 다르게 내용 변경이나 추가를 할 수 없지만 속도가 list보다 빠르다.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") #튜플은 추가가 불가능
# name = "김종국"
# age = 20
# hobby = "코딩"

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 집합 set, 중복안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1,2,3}

java = {"유재", "조세", "박명"}
python = set(["유재", "박명"])
# 교집합
print(java & python)  # 유재
print(java.intersection(python))  # 유재

# 합집합
print(java | python)
print(java.union(python))

# 차집합 java는 가능, python은 불가능
print(java - python)
print(java.difference(python))  # 조세, 박명
java.remove("박명")

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))  # {커피, 우유, 주스} , <class 'set'>

menu = list(menu)  # list로 바뀜 []
menu = tuple(menu)  # tuple로 바뀜 ()

weather = "비"

if weather == "비" or weather == "눈":  # or
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크 챙겨")
else:
    print("it's good")

weather = input("오늘 날씨는?")  # 입력을 기다린다.

temp = int(input("기온은 어때요?"))  # input은 문자열으로 받기 때문에 받아서 int로 바로 저장
# str 입력하면 ValueError 발생
if 30 <= temp:
    print("don't go out")
elif 10 <= temp and temp < 30:  # and
    print("It's so so")
elif 0 <= temp < 10:  # and
    print(" little cold ")
else:
    print("춥당")

# for 반복문
print("대기번호 : 1")

for waiting_num in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_num))  # 0, 1,2,3,4 순서대로 들어감

for waiting_num in range(1, 5):  # 1에서부터 5미만까지
    print("대기번호 : {0}".format(waiting_num))  # 1,2,3,4 순서대로 들어감

starbucks = ["재석", "박명", "조세"]
for customer in starbucks:
    print("{0}, 커피 준비됨".format(customer))

# while 반복문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피 준비됨. {1}번안에 와라".format(customer, index))
    index -= 1
    if index == 0:
        print("커피 버렸어요")

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피 준비됨.".format(customer))
    person = input("이름이 어떻게 되세요? ")  # 토르면 종료됨

absent = [2, 5]
book = [4]
for student in range(1, 11):
    if student in absent:
        continue  # 넘기고 계속 진행해
    elif student in book:
        print("오늘 수업 여기까지 {0}는 교무실로 와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생이름을 길이로 변환
students = ["abcd", "abc", "abcdefgh"]
upperstudent = [e.upper() for e in students]
students = [len(i) for i in students]

cnt = 0  # 총 탑승객 수
for i in range(1, 5):
    time = randrange(5, 51)  # 5~50분 사이 소요 시간
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 ( 소요시간 : {1}분 )".format(i, time))
        cnt += 1
    else:
        print("[x] {0}번째 손님 ( 소요시간 : {1}분 )".format(i, time))

print(f"총 승객수 : {cnt}")

# 함수


def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance: int, money: str) -> int:  # str이 money에 들어가도 에러는 발생하지 않는다.
    print(f"입금이 완료 되었습니다. 원래 잔액은 {balance}원 입니다.")
    return balance + money, balance


balance = deposit(1000, 100)
print(balance)
balance, originalmoney = deposit(500, 100)  # return값을 2개해도 이렇게 구동이 된다.


def profile(name, age=17, lang="Python"):  # default arguement설정.
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
          .format(name, age, lang))  # 역슬래쉬로 줄바꿔서 이어가기


profile("김호진")  # non-default가 default뒤에 오면 안된다.


def profile(name, age, lang):
    print(name, age, lang)


# 순서가 바껴도 keyword써서 parameter 전달하면 가능.
profile(lang="js", name="hojin", age=23)


def longpro(name, age, lang1, lang2, lang3, lang4):
    print("이름 : {0}\t나이 : {1}".format(name, age), end=" ")  # 역슬래쉬로 줄바꿔서 이어가기
    print(lang1, lang2, lang3, lang4)


longpro("나", "23", "c", "", "", "")  # ""를 여러번 해줘야 한다.


def longprofile(name, age, *language):  # 가변 인자 language
    print("이름 : {0}\t나이 : {1}".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


longprofile("나", 23, "c", "java")
longprofile("너", 13, "c", "java", "python")  # 가변인자

gun = 10


def checkpoint(soldiers):
    # gun = 10  이걸 추가 하거나
    global gun  # 전역변수인 gun을 함수내에서 쓰겠다는 뜻.
    gun -= soldiers  # 이건 지역변수 gun이다. 따라서 위 라인을 추가해줘야함
    print(f"남은 총 :{gun}")


print(gun)  # 10
checkpoint(2)  # 8
print(f"남은 총 :{gun}")  # 8


def checkpoint_ret(gun, soldiers):
    gun -= soldiers
    print(gun)
    return gun


gun = checkpoint_ret(gun, 2)
#
#
# 가급적 global키워드의 활용 보다는 함수의 parameter로 던져서 return으로 저장하는게 낫다.
#
#


def std_weight(ki: int, gender: str):
    if gender == "male":
        print(round(ki*ki*22, 2))
    elif gender == "female":
        print(round(ki*ki*21, 2))  # 소수점 둘째자리 까지만 표시해줘! -> 셋째자리에서 반올림
    else:
        print("올바른 성별을 입력해 주세요")


ki = int(input("키를 입력해주세요"))
gender = input("성별")

std_weight(ki/100, gender)

print("Python", "Java", "Javascirpt", sep=",", end="?")
# 사이를 sep로 이어줌. #end로 끝내고 줄바꿈을 하지 않는다.
print("Python", "Java", file=sys.stdout)  # 표준 출력
print("Python", "Java", file=sys.stderr)  # 표준 에러

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():  # subject가 key가 되고 score가 value가 됨
    # ljust는 왼쪽으로 정렬을 하는데 8칸을 확보한 상태에서.
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 11):
    print(str(num).zfill(3))  # 3칸 확보하고 나머지는 0으로 채우자

# answer = input("아무값이나 입력하세요 : ")
# print(type(answer)) #항상 문자열로 저장

# 빈자리는 빈공간으로 두고, 오른쪽 정렬, 10칸 확보
print("{0: >10}".format(500))
# 양수는 +로 표시
print("{0: >+10}".format(500))
# 왼쪽 정렬하고, 빈칸은 _로 채움
print("{0:_<10}".format(500))
# 3자리마다 콤마를 찍어주고 양수는 + 붙이기
print("{0:+,}".format(1000000))

print("{0:ㅎ<+15,}".format(1000000))

# 소수점 출력 두번째 자리수 까지만 - 셋째 자리에서 반올림
print("{0:.2f}".format(5/3))

# 파이썬을 통해서 컴퓨터내의 파일 사용하기

# w : 쓰기위한 용도 이미 존재한다면 덮어쓰게 된다.
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 10", file=score_file)
score_file.close()  # 파일을 열었으면 꼭 닫아줘야한다.

score_file = open("score.txt", "a", encoding="utf8")  # a : 쓰는데 추가해서 쓴다
score_file.write("과학 : 80")
score_file.write("\n코딩 : 80")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # utf8이 한글을 잘 다룸
print(score_file.read())
score_file.close()

score_file.open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())  # 4번하면 다 읽는데 몇줄인지 모른다면?
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
print(lines)  # ['수학 : 0\n', '영어 : 10\n', '과학 : 80\n', '코딩 : 80']로 저장된다
score_file.close()

# 피클! 프로그램상에서 사용하고 있는 데이터를 파일로 저장해주는것
profile_file = open("profile.pickle", "wb")  # b는 binary를 의미
profile = {"이름": "박명수", "나이": "30", "취미": ["축구", "골프"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 profile_file에 저장한다.
profile_file.close()  # 저장한걸 열어보면 binary라서 읽을 수 없다고 뜬다.

profile_file = open("profile.pickle", "rb")  # b는 binary를 의미
profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with! with를 쓰면 파일을 엵고 닫는게 편리하다

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    # with문을 탈출하면서 자동으로 종료

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부 중")

for i in range(1, 5):
    #report = open(f"{i}주차.txt", "w", encoding="utf8")
    #report.write(str(i) + "주차 보고서 입니다.")
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 - \n".format(i))
        report_file.write("끝입니다.")
    report_file.close()

report_file = open("4주차.txt", "r", encoding="utf8")
print(report_file.readline())
report_file.close()

Class 파트 입니다!

마린

name = "마린"
hp = 40
damage = 5

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력은 {hp}, 공격력은 {damage}")

tank_name = "탱크"
tank_hp = 40
tank_damage = 5

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력은 {tank_hp}, 공격력은 {tank_damage}")


def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 공격합니다. [공격력 {damage}]")

# 일반 유닛


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def Move(self, location):
        print("[지상유닛이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

# marine1 = Unit("마린","40","5")

# # __init__ : 생성자. 객체(class로 만들어지는)가 만들어질때 자동으로 호출되는 부분.
# #self 제외하고 parameter 갯수만큼 argument를 전달해줘야한다.

# wraith1 = Unit("레이스", 80, 10)
# print(f"유닛 이름은 {wraith1.name}고, hp는 {wraith1.hp}이다. ")

# wraith2 = Unit("뺏은 레이스", 80, 11)
# wraith2.clocking = True #class 정의 시에 없었던 property를 객체에 추가할 수 있다.
# # 확장
# if wraith2.clocking == True:
#     print(f"{wraith2.name}은 현재 클로킹 상태입니다.")

# 공격 유닛


class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)  # Unit에 있는거 다 써야함
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력은 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name}유닛이 {damage}데미지를 받았습니다.")
        self.hp -= damage
        print(f"현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name}이 파괴되었습니다. 퍼펑!")


firebat = AttackUnit("파이어뱃", 40, 15, 5)

firebat.attack("5시")  # self는 전달 안해줘도 됨.
firebat.damaged(25)
firebat.damaged(25)

# 상속
# Unit에 있는 variable과 method는 그대로 AttackUnit에 전달해줄 수 있다.

# 다중 상속 부모 class를 2개 이상 받는 것


class Flyable:
    def __init__(self, flyspeed):
        self.flyspeed = flyspeed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flyspeed}]")
#
# 여기서 flyspeed 대신 self.speed 썼는데 2라고 된다!

#


class AttackFlyUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyspeed):
        AttackUnit.__init__(self, name, hp, damage, 2)
        Flyable.__init__(self, flyspeed)

    def Move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)


valkyrie = AttackFlyUnit("발키리", 50, 20, 5)
valkyrie.fly(valkyrie.name, "3시")  # 상속받은 Method도 바로 사용가능.

# Method Overriding 자식클래스에서

vulture = AttackUnit("벌쳐", 30, 8, 20)

BattleCruiser = AttackFlyUnit("배틀크루져", 200, 40, 15)

# 563줄에 따라서 AttackFlyUnit안에 speed를 정의하지 않아도 AttackUnit안에 있는 speed variable을 사용 가능하다.
print(BattleCruiser.speed)

vulture.Move("12시")
BattleCruiser.fly(BattleCruiser.name, "9시")
# 지상, 공중 따로하기 너무 귀찮다ㅠㅠ

BattleCruiser.Move("3시")
# AttackFlyUnit에서 재정의된 Move 함수

# pass


class BuildingUnit(Unit):  # Unit class를 상속받는다.
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)  # 위 라인과 똑같지만 self는 없이 쓴다.
        # 다중상속이면 앞에 적은거만 상속.
        self.location = location

    def destroyed(self):
        pass  # 아무것도 안하고 일단은 넘어간다. 완성된것 처럼.


supplydepot = BuildingUnit("서플라이디폿", 500, "7시")
# print(supplydepot.name)  #이건 당연히 오류 뜬다
supplydepot.destroyed()  # 오류없이 넘어감

# super
#        super().__init__(name, hp, 0) #위 라인과 똑같지만 self는 없이 쓴다.

"""
람다 표현식 : 식별자 없이 실행 가능한 함수를 말하며, 가독성은 낮다
함수의 선언 없이도 하나의 식으로 함수를 단순하게 표현하는것. 리스트 컴프리헨션이 더 좋긴 함

s = ['1 A', '1 B', '2 A', '2 B']
sorted(s) -> 1a, 1b, 2a, 2b 인데 그 뒤의 문자순의 정렬을 원한다면,

s.sort(key=lambda x: (x.split()[1], x.split()[0]))
원래 s.sort()에 key를 지정해줘서 할 수 있다. key는 뭘 잡아서 정렬하는지를 의미.

"""
# 정규식 습득하자!
"""
re.sub("찾을 문자열", "변경 할 문자열", 대상)
#문자열을 변경한다.
ex = "this is test, Rabbit is Cute"
Text = re.sub("Rabbit", "Cat", ex)
결과 :  "this is test, Cat is Cute"
#찾을 문자열 끝에 기호 '+'를 붙일 경우 이어지는 문자열을 하나의 문자로 간주한다.
ex = "My card is BBBB"
Text = re.sub("B+", "A", ex)
결과 : "My card is A"

"""
