# include <iostream> //전처리 지시자

/*
c++에서 함수를 사용하고자  한다면 반드시 그 함수의 원형을 미리 정의해야 한다.
*/
using namespace std;

int main(){

    int a; // 선언
    a = 7; // 대입
    int b = 10; // 초기화
    {
        int b;
        {
            int a;
            b = 5;
        }
        a = 7; // Error!
    }

    cout << "Hello, World!" << a << endl;

    cout << a << endl;

    return 0;
}
