패키지 : 모듈을 모아 놓은 것 직접 파이썬 패키지로 만들어서 누구나 사용할 수 있도록 하자.
import travel.japan #class나 함수는 바로 import 할 수 없다! module만 가능. 
# from import로는 class나 함수 import 가능
trip_to = travel.japan.JapanPackage()
trip_to.detail()

from travel import newyork
trip = newyork.NewyorkPackage()
trip.detail()

# __all__ : * 같은
from travel import *
trip_to = japan.JapanPackage() # 오류난다. 개발자가 문법상에서 공개/비공개 설정을 안해서. __init__ 으로 가세요
#pylint 해제 : File -> setting -> preference -> linting검색해서 python-linting Enabled
trip_to.detail()

실제로 패키지나 모듈 만들때는 잘 동작하는지 테스트가 필요하다.

import inspect
import random
print(inspect.getfile(random)) #모듈을 가져온 위치의 경로를 가르킴 이 위치에 travel을 놓아도 실행 가능
print(inspect.getfile(japan)) 
# C:\Python38\lib\random.py
# C:\Python38\lib\travel\japan.py



pip로 존재하는 패키지 설치하기! 사람들이 잘 만들어 놓은거 활용해야지?
terminal에서  pip install beautifulsoup4  와 같이 사용.

내장 함수. 내장되어 있어서 import 할 필요 없는 함수.. ex) input, print
dir : 어떤 객체를 넘겨줬을 때 객체가 어떤변수와 함수를 가지고 있는지 알려주는것.

외장 함수 : import 해서 사용해야 하는것. list of Python modules를 구글에 검색해서 확인할 수 있다 ex) random





