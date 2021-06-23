
from bs4 import BeautifulSoup
import requests

LIMITNUM = 10
URL = "https://kr.indeed.com/jobs?q=Python&l="


def extract_indeed_pages():
    result = requests.get(URL)

    print(result)  # Response[200] 면 ok
    # html code를 살펴본다. indeed_result.text 붙이면 됨
    # beautiful soup4 pip install 하자!

    # page수 뽑아내기 시작
    soup = BeautifulSoup(result.text, "html.parser")  # html_cod, html.parser

    # print(soup) soup에 페이지의 html이 다 저장됨.

    # 뷰티풀수프로 데이터 구조를 탐색할 수 있다. 뷰수 홈페이지에서 사용가능한 method들 볼 수 있음.
    pagination = soup.find("div", {"class": "pagination"})
    # print(pagination)

    pages = pagination.find_all('a')
    # print(pages)
    page_list = []
    for page in pages[:-1]:
        # page_list.append(page.find("span").string) #드디어 가져왔다 #string은 안의 텍스트만 추출
        page_list.append(int(page.string))  # bs4가 자동으로 찾아준다.

    # print(page_list[0:-1]) # 마지막꺼 빼고 출력.
    print(page_list)
    """페이지 수 : page_list[-1]
    """
    max_page = page_list[-1]
    return max_page


def extract_indeed_jobs(last_page):  # 몇개의 페이지를 request할지
    jobs = []
    numbb = 0
    for page in range(last_page):
        # 숫자대신 미리 선언한 변수를 사용해서 더 보기좋게 만들어준다.
        result_request_many_pages = requests.get(
            f"{URL}&start={page*LIMITNUM}")
        # html_code, html.parser 각 페이지의 html코드
        soup = BeautifulSoup(result_request_many_pages.text, "html.parser")
        # div 중 class명이 j~ 인것.
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        # print(results)
        for want in results:
            job = extract_title_company(want)
            jobs.append(job)
        # print(result_request_many_pages) #<Response [200]> 이 자동을 5번 출력. -> 자동으로 페이지 5개를 훑었다.
        print(f"{page + 1}번째 페이지 탐색완료")
    return jobs

# 2.8 영상 11:30 이후에 콘솔창의 링크를 클릭 했을 때 'page not find'라는 페이지가 나오면 &from=web&vjs=3 이걸 넣어주세요. 사이트의 변화가 계속있어서 그런 것 같습니다.


def extract_title_company(html):
    # title = want.find("h2", {"class":"title"}) #class가 title인 h2
    # anchor = title.find("a")["title"] # a의 attribute중 title을 가져온다.
    title = html.find("h2", {"class": "title"}).find("a")["title"]

    # html.find("h2", {"class":"title"}).find("a") 의 <<이게 하나의 덩어리 attribute중 title을 가져온다.
    # company = want.find("span", {"class":"company"}).find("a").string #company중에 a가 없는게 하나라도 있으면 오류 발생
    # 그래서 if else로 구분해줘야 한다.
    company = html.find("span", {"class": "company"})
    ca = company.find("a")
    if ca is not None:
        company = (str(ca.string))
    else:
        # 문장사이에 빈칸한줄씩 있는걸 없애주려고 한다. get_text는 .string의 역할, strip=True는 지워줌
        company = str(company.string)
        # .strip("지울거") 를 추가로 붙여줄 ㅅ ㅜ있음
    company = company.strip()  # strip은 안에 적은걸로 시작하는걸 없애준다

    location = html.find("span", {"class": "location"})
    if location is not None:
        location = location.string
    job_id = html["data-jk"]  # 바로 []로 하는건 뭐지??
    # 뽑아낸 div(여기선 html) 안의 data-jk attribute를 가져왔다.
    for_return = {'직군': title, '회사': company, '위치': location,
                  '지원링크': f"https://kr.indeed.com/viewjob?jk={job_id}"}
    return for_return
