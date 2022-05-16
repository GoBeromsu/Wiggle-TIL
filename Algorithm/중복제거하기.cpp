#include <stdio.h>
#include <set>
#include <iostream>

using namespace std;

int main()
{
    int N; // 반복 횟수를 입력 받는다.
    cin >> N;

    set<int> integers; // 정수를 저장할 집합을 선언한다.
    for (int i = 0; i < N; ++i)
    {
        int x; //순차적으로 집합에 숫자를 입력한다.
        cin >> x;

        if (integers.count(x) > 0) // 이미 집합에 들어가 있는 경우에는 Duplicated를 출력한다.
        {
            cout << "DUPLICATED\n";
        }
        else
        {
            integers.insert(x); // 집합에 값이 없으므로 입력 받은 숫자를 넣고, OK를 출력한다.
            cout << "OK\n";
        }
    }
    return 0; //프로그램을 종료합니다.
}