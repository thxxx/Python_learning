import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w",  encoding = "utf-8") # utf-8 하면 한글이 안깨짐
    # mode = "w" 는 새로 덮어쓴다.
    # csv 작성 시작.
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"]) # 우리가 jobs에서 return받는 dict
    # list로 써야한다.
    for job in jobs:
        #job의 value 들만을 가져오길 'title' 은 말고. 원한다.
        writer.writerow(list(job.values())) 
        # writer.writerow(list(job.values())) # 원래 타입은 dict_values라는 특이 type
    return


 # csv를 다루는 기술
