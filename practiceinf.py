# from random import * #random에서 *은 전부 다 import 한다는 걸 의미.

# # class Unit:
# #     def __init__(self):
# #         print("Unit 생성자")

# # class Flyable:
# #     def __init__(self):
# #         print("Unit 생성자")

# # class FlyableUnit(Unit, Flyable): #2개를 상속?
# #     def __init__(self):
# #         super().__init__()
# #         #Unit.__init__(self)
# #         #Flyable.__init__(self)
# # dropship = FlyableUnit() # -> super를 쓰면 앞에있는 Unit 생성자만 호출된다.

# #일반 유닛 

# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 공격합니다. [공격력 {damage}]")

# # 일반 유닛 class 정의
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def Move(self, location):
#         print("[지상유닛이동]")
#         print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")
       
# # marine1 = Unit("마린","40","5")

# # # __init__ : 생성자. 객체(class로 만들어지는)가 만들어질때 자동으로 호출되는 부분.
# # #self 제외하고 parameter 갯수만큼 argument를 전달해줘야한다.

# # wraith1 = Unit("레이스", 80, 10)
# # print(f"유닛 이름은 {wraith1.name}고, hp는 {wraith1.hp}이다. ")

# # wraith2 = Unit("뺏은 레이스", 80, 11)
# # wraith2.clocking = True #class 정의 시에 없었던 property를 객체에 추가할 수 있다. 
# # # 확장
# # if wraith2.clocking == True:
# #     print(f"{wraith2.name}은 현재 클로킹 상태입니다.")

# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage, speed):
#         Unit.__init__(self, name, hp, speed) #Unit에 있는거 다 써야함
#         self.damage = damage
        
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력은 {self.damage}]")
    
#     def damaged(self, damage):
#         print(f"{self.name}유닛이 {damage}데미지를 받았습니다.")
#         self.hp -= damage
#         print(f"현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name}이 파괴되었습니다. 퍼펑!")

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가 체력 10써서
#     def stimpack(self): #self로 받는 이유?
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소) ".format(self.name))
#         else:
#             print("{0} : 체력이 부족합니다.")

# # 탱크 
# class Tank(AttackUnit):
    
#     seizemode_developed = False
        
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 100, 20, 5)
#         self.seize_mode = False
    
#     #시즈모드 
#     def siezemode(self):
#         if Tank.seizemode_developed == False: # 바로 Tank.으로 사용한다.
#             return
#         if self.seize_mode == False:
#             print(f"{self.name}이 시즈모드로 전환합니다.")
#             self.damage *= 2
#             self.seize_mode = True
        
#         else : 
#             print(f"{self.name} : 시즈모드를 해제합니다.")
#             self.damage /= 2
#             self.seize_mode = False

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)

# for unit in attack_units:
#     unit.Move("1시")

# Tank.seizemode_developed = True
# print("탱크 시즈모드 준비 완료")

# for unit in attack_units:
#     #새로운거! 지금 만들어진 객체가 어떤 class의 인스턴스인지 확인하는 것.
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.siezemode()

# for unit in attack_units:
#     unit.attack("1시")

# for unit in attack_units:
#     unit.damaged(randint(25,91)) # 2~20 사이 랜덤 데미지
# game_over()
"""
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
"""

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = "아파트"
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} \
        {self.price} {self.completion_year}")

ma1 = House("강남", "아파트", "매매", "10억", "2010년")
ma2 = House("마포", "빌라", "전세", "5억", "2007년")
ma3 = House("송파", "오피스텔", "월세", "500/50", "2000년")

# houselist = []
# houselist.append(ma1)
# houselist.append(ma2)
# houselist.append(ma3)

# print(f"총 {len(houselist)}개의 매물이 있습니다.")
# for house in houselist:
#     house.show_detail()

# def delee():
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# #예외처리
# try:
#     delee()
# except ValueError: # 에러 발생시 다시 try 하려면??
#     print("숫자를 입력하셔야 해요.")
# except ZeroDivisionError as err: #err은 발생하는 에러 문장.
#     print(err)
#     print("0으로는 나눌수 없어요.")
# except Exception as err: # 뭔지는 특정하지 못하고 에러문장을 err로
#     print(f"무언가 {err}가 발생했어요!")
# finally:
#     print("어쨌든 난 내 할일 함")

# 컨트롤 / 하면 전체 주석처리

#의도적인 에러 발생

#파이썬 에서 미리 제공하는 에러 말고 직접 정의하기
# class BigNumberError(Exception):
#     def __init__(self,msg): # 이거 안하고 pass로만 둬도 된다.
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2)) #바로 해당 에러 처리구문으로 이동
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except BigNumberError as err: # 입력한 에러 메시지가 err로 처리된다.
#     print("한자리 숫자만 입력가능합니다.")
#     print(err)

#퀴즈

# chicken = 10
# waiting = 1 # 홀안에는 현재 만석, 대기번호 1부터 시작

# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg
    
# while(True):
#     try:
#         print(f"[남은 치킨:{chicken} ]")
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 많이 주문했을 때
#             raise SoldOutError("재료가 부족합니다 죄송합니다.")
#             #print("재료가 부족합니다 죄송합니다.")
#         elif order < 1:
#             raise ValueError
#         else :
#             print(f"[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다.")
#             waiting += 1
#             chicken -= order
#     except SoldOutError as err:
#         print(err)
#         break # while문 탈출

#     except ValueError:
#         print("1이상의 숫자만을 입력하셔야 합니다.")

# 모듈! 필요한 부품끼리 모아져있는 파일 class 등을 담고 있는 파일






