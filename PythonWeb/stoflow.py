import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://stackoverflow.com/jobs?q=python&sort=y"

result = requests.get(URL)
print(result)

soup = BeautifulSoup(result.text, "html.parser")

def get_last_page():
    pagination = soup.find("div", {"class" : "s-pagination"}).find_all("a")
    page_list = []
    pagination = pagination[0:-1]
    pages = pagination[-1]
    # for page in pagination[:-1]:
    #     page_list.append(int(page.string))
    last_page = pages.get_text(strip = True)
    return int(last_page)

def extract_jobs(last_page):
    jobs = []
    number = 0

    for page in range(last_page): #page is the number of 현재 페이지
        many_pages = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(many_pages.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            # print(result["data-jobid"]) #data-res
            job = extract_detail(result)
            jobs.append(job)
        # print(f"{page + 1}번째 페이지 탐색완료")
    return jobs

def extract_detail(html):
    title = html.find("h2", {"class":"mb4 fc-black-800 fs-body3"})\
        .find("a")["title"]
    company, location = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"})\
            .find_all("span", recursive=False)
    #unpacking value라고 한다. 리스트안에 2개만 들어있다는걸 알고 있을 때 쓰는 방법.
    if company is not None:
        company = str(company.get_text(strip=True))
    else :
        company = None
    location = location.get_text(strip=True) # - 가 추가되어있으면 .strip("-") 을 붙여서 지울 수 있다.
    job_id = html['data-jobid'] # 여기서 html은 div의 html 코드.
    return {"title":title, 
    "company":company, 
    "locatin":location, 
    "apply_link":f"https://stackoverflow.com/jobs/{job_id}"}



def get_so_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(2)
    return jobs

get_last_page()
get_so_jobs()