# # For machine learning, Data Science 구글 크롬 사용해야 한다.

from bs4 import BeautifulSoup
import requests


# # 첫번째 파트. 파이썬 프로그래밍 이론
# a_string = "like this"
# a_bool = True
# days = ['Mon', 'Tue', 'Wed']
# days.append('Sat')
# days.reverse()

# #immutable tuple 수정 불가능.
# days_tu = ('Mon', 'Tue', 'Wed')
# print(type(days_tu))

# #dict key와 value를 가짐
# hojin = {
# "name" : "Hojin",
# "age" : 29,
# "korean" : True,
# "fav_food" : ["Kimchi", "Sashimi"]
# }
# print(hojin["name"])
# hojin["smart"] = True
# print(hojin)

# #built-in function
# def say_hello(who, a = 0): #arguement를 하나만 전달하면 default로 0을 줘라
#     # print(f"Hello {who}! {a} times ")
#     return f"{who} Hi {a}"

# say_hello("go")
# name = say_hello("go")
# print(name)

# #Positional 인자, Keyworded 인자 순서에 헷갈리지 않아도 된다.
# say_hello(a=30, who="hojin")

# def plus(a, b):
#     if type(b) is not int and type(b) is not float:
#         return None
#     else :
#         return int(a) + int(b)
# plus_result = plus(12, 15)
# print(plus_result)

# for i in days_tu :
#     print( i + "sday") #어떻게 print는 무한으로 인자를 받을 수 있을까?


# 두번째 파트. 웹 프로젝트 Web scraping
# url로 부터 사진과 제목을 가져온다.
# url로 접근 -> 페이지가 몇개인지 알아낸다. -> 하나씩 들어간다.

# request 설치 by pip install requests

# indeed_result = requests.get("https://kr.indeed.com/jobs?q=Python&l=")

# print(indeed_result) #Response[200] 면 ok
# #html code를 살펴본다. indeed_result.text 붙이면 됨
# #beautiful soup4 pip install 하자!

# #page수 뽑아내기
# indeed_soup = BeautifulSoup(indeed_result.text, "html.parser") # html_cod, html.parser
# #print(indeed_soup)

# # 뷰티풀수프로 데이터 구조를 탐색할 수 있다. 뷰수 홈페이지에서 사용가능한 method들 볼 수 있음.
# pagination = indeed_soup.find("div", {"class":"pagination"})
# #print(pagination)

# pages = pagination.find_all('a')
# #print(pages)
# page_list = []
# for page in pages[:-1]:
#     #page_list.append(page.find("span").string) #드디어 가져왔다 #string은 안의 텍스트만 추출
#     page_list.append(int(page.string)) #bs4가 자동으로 찾아준다.

# #print(page_list[0:-1]) # 마지막꺼 빼고 출력.
# print(page_list)
# """페이지 수 : page_list[-1]
# """
# max_page = page_list[-1]

from indeed import extract_indeed_pages, extract_indeed_jobs
from stoflow import *
from save import save_to_file

# 페이지를 계속해서 request하는법. 페이지 갯수만큼 해줘야하지?


def get_indeed_jobs():
    last_indeed_pages = extract_indeed_pages()
    jobs = extract_indeed_jobs(2)
    return jobs

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()

all_jobs = so_jobs + indeed_jobs

print(all_jobs)

# 이제 이 all_jobs를 excel sheet에 넣는다

# save_to_file(all_jobs)  # all_jobs

# 세번째 파트. django web framework 사용하기 위해 알면 좋은 것들
