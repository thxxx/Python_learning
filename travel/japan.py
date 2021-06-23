class JapanPackage:
    def detail(self):
        print("[일본 패키지 3박 4일] 오사카, 나라 여행 (신사 투어) 50만원")


if __name__ == "__main__":
    trip_to = JapanPackage()
    trip_to.detail()
    print("Japan 모듈을 직접 실행")
    print("이 문장을 모듈을 직접 실행할 때만 실행돼요")
else : 
    print("Japan 외부에서 모듈 호출.")

#모듈 외부에서 이걸 가져다 쓰는건지 파악하는데 도움을 준다.