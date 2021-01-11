# 일반 가격
def price(people):
    print(f"{people}명 가격은 {people*10000}원 입니다.")

def price_morning(people):
    print(f"{people}명의 조조할인 가격은 {people*6000}원 입니다.")


def price_army(people):
    print(f"{people}명의 군인 할인 가격은 {people*5000}원 입니다.")

if __name__ == "__main__":
    print("Japan 모듈을 직접 실행")
    print("이 문장을 모듈을 직접 실행할 때만 실행돼요")
else : 
    print("Japan 외부에서 모듈 호출.")

price(3)
