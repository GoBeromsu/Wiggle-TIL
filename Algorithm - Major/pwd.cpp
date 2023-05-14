#include <stdio.h>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
#include <time.h>
#pragma warning(disable : 4996)
using namespace std;

map<int, vector<int>> posMap;  // 한 번호에 인전합 번호들을 저장할 맵입니다.
vector<bool> check(10, false); // 해당 번호를 갔는지 체크할 벡터입니다.

// 각 번호가 갈 수 있는 인접한 번호를 저장핧 맵을 초기화합니다.
void makeMap()
{
    posMap[1] = vector<int>{2, 4, 5};
    posMap[2] = vector<int>{1, 3, 4, 5, 6};
    posMap[3] = vector<int>{2, 5, 6};
    posMap[4] = vector<int>{1, 2, 5, 7, 8};
    posMap[5] = vector<int>{1, 2, 3, 4, 6, 7, 8, 9};
    posMap[6] = vector<int>{2, 3, 5, 8, 9};
    posMap[7] = vector<int>{4, 5, 8};
    posMap[8] = vector<int>{4, 5, 6, 7, 9};
    posMap[9] = vector<int>{5, 6, 8};
}

bool process(int L, vector<int> number)
{
    check[number[0]] = true; //입력 값의 첫 번째 번호에서 시작하므로 체크해줍니다.
    for (int i = 1; i < L; i++)
    {
        int currentNum = number[i];                        // 현재 도착한 번호 입니다.
        int beforeNum = number[i - 1];                     // 이전에 있던 번호입니다.
        for (int j = 0; j < posMap[beforeNum].size(); j++) //
        {
            if (currentNum == posMap[beforeNum][j]) // 현재 번호가 이전 번호가 이어져 있는지 확인을 하고, 왔음을 체크합니다.
            {
                check[currentNum] = true;
                break; // 체크가 끝났으므로 바로 다음 연산을 준비합니다.
            }
            else if (check[currentNum] == true)
            {
                //이미 들린 곳을 또 가려고 할 때 이므로 false를 반환합니다.
                return false;
            }
        }
        // 위의 반복문은 이어진 노드 간의 관계를 확인하는 것이었습니다.
        // 아래 조건문은 직접적으로 이어지지 않는 (4-6)를 이을 때의 조건을 확인하는 역할 입니다.
        if (check[currentNum]) //이미 방문했던 곳의 경우를 제외 합니다, 아래 조건문에서 걸러질 수 있기 때문입니다.
        {
            continue;
        }
        else if (check[(beforeNum + currentNum) / 2] && float(beforeNum + currentNum) / 2 == 0)
        {
            // 두 점 사이의 중점을 가본 적이 있다면, 갈 수 있는 점이므로 체크합니다.
            check[currentNum] = true;
        }
        else
        {
            // 갈 곳이 없는 경우이므로 false를 반환합니다.
            return false;
        }
    }

    return true; // 위의 반복문을 모두 통과하면, 경로가 존재하므로 참을 반환합니다
}

int main()
{

    int L = 0;
    scanf("%d", &L); // 번호의 갯수를 입력 받습니다.

    vector<int> number(L, 0); // 가야할 경로(번호)를 입력 받습니다.
    for (int i = 0; i < L; i++)
    {
        scanf("%d", &number[i]);
    }

    makeMap(); // 전화번호가 갈 수 있는 인전 노드를 정의합니다.
    // 실행 시간 계산에 쓰일 변수를 선언한다.
    clock_t start, finish;
    double duration;
    start = clock();
    // 경로를 갈 수 있는 경우 YES를, 아닐 경우 NO를 출력합니다.
    if (process(L, number))
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

    // 출력
    // 실행 시간과 결과 값을 출력합니다.
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;

    cout << "실행시간: " << duration << "초" << endl;
}
