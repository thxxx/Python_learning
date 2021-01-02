# import theater_module
# theater_module.price(3) #3명이서 영화보러 갔을 때 가격

# theater_module.price_morning(4)
# theater_module.price_army(2)

# #모듈은 그냥 파이썬 파일.
# import theater_module as mv #별명을 붙여서 mv로 사용.
# mv.price_army(2)

# from theater_module import *
# # 모듈안의 class 나 함수를 그냥 바로 사용하겠다.

#원하는 것만 임포트 가능.
from theater_module import price, price_morning

#원하는 걸 줄여서 별명으로 사용
from theater_module import price_army as price
price(3)

