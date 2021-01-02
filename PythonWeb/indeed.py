
from bs4 import BeautifulSoup
import requests

LIMITNUM = 10
URL = "https://kr.indeed.com/jobs?q=Python&l="

def extract_indeed_pages():
    result = requests.get(URL)

    print(result) #Response[200] 면 ok
    #html code를 살펴본다. indeed_result.text 붙이면 됨
    #beautiful soup4 pip install 하자!

    #page수 뽑아내기
    soup = BeautifulSoup(result.text, "html.parser") # html_cod, html.parser
    #print(soup)

    # 뷰티풀수프로 데이터 구조를 탐색할 수 있다. 뷰수 홈페이지에서 사용가능한 method들 볼 수 있음.
    pagination = soup.find("div", {"class":"pagination"})
    #print(pagination)

    pages = pagination.find_all('a')
    #print(pages)
    page_list = []
    for page in pages[:-1]:
        #page_list.append(page.find("span").string) #드디어 가져왔다 #string은 안의 텍스트만 추출
        page_list.append(int(page.string)) #bs4가 자동으로 찾아준다.
        
    #print(page_list[0:-1]) # 마지막꺼 빼고 출력.
    print(page_list)
    """페이지 수 : page_list[-1]
    """
    max_page = page_list[-1]
    return max_page


def extract_indeed_jobs(last_page):  #몇개의 페이지를 request할지
    jobs = []
    for page in range(last_page):
        result_request_many_pages = requests.get(f"{URL}&start={page*LIMITNUM}")  # 숫자대신 미리 선언한 변수를 사용해서 더 보기좋게 만들어준다.
        print(result_request_many_pages) #<Response [200]> 이 자동을 5번 출력. -> 자동으로 페이지 5개를 훑었다.
     return jobs







