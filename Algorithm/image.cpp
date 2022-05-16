#include <iostream>
#include <vector>
#include <stdlib.h>
#include <map>
#include <time.h>
#include <string>
#include <algorithm>

using namespace std;
map<int, string> bitMap; //주어진 비트에 해당하는 코드를 맵핑하는 map입니다.

// 비트 코드 map을 정의합니다.
void makeMap()
{
    bitMap[1] = "00";
    bitMap[86] = "01";
    bitMap[172] = "10";
    bitMap[256] = "11";
}

int main()
{
    //가중치와 숫자의 갯수를 입력 받습니다.
    int N, W;
    cin >> N >> W;
    // 비트 코드 map을 정의합니다.
    makeMap();

    // 수열을 순차적으로 입력 받습니다.
    vector<int> numbers(N, 0);

    for (int i = 0; i < N; i++)
    {
        cin >> numbers[i];
    }

    // 이진 비트들의 level을 연산의 편의를 위해 선언해둡니다.
    int bitCode[4] = {1, 86, 172, 256};

    // 변환 비용을 저장할 N X 4 크기의 벡터를 선언합니다.
    vector<vector<int>> cost(N);
    // 이중 벡터의 각 크기를 주어진  레벨의 갯수만큼으로 초기화 합니다.
    for (int i = 0; i < N; i++)
    {
        cost[i].resize(4, 0);
    }
    string answer = "";// 코드를 저장할 문자열을 선언합니다.
    int beforeMin = 0;// 이전 회차의 최솟 값을 저장할 변수 입니다.
    int currentMin = 0;// 현재 회차의 최솟 값을 저장할 변수 입니다.
    int beforeMinIndex = 0;//
    int currentMinIndex = 0;
    // 실행 시간 계산에 쓰일 변수를 선언한다.
    clock_t start, finish;
    double duration;
    start = clock();

    for (int i = 0; i < N; i++)
    {

        if (i == 0)
        {
            for (int j = 0; j < 4; j++)
            {
                cost[i][j] = abs(numbers[i] - bitCode[j]) + W * 2;
            }
            beforeMin = *min_element(cost[i].begin(), cost[i].end());
            beforeMinIndex = find(cost[i].begin(), cost[i].end(), beforeMin) - cost[i].begin();
            answer += bitMap[bitCode[beforeMinIndex]];
            continue;
        }
        for (int j = 0; j < 4; j++)
        {
            if (j == beforeMinIndex)
            {
                //이전과 같은 에러일 경우
                cost[i][j] = beforeMin + W + abs(numbers[i] - bitCode[j]);
            }
            else
            {
                cost[i][j] = beforeMin + 3 * W + abs(numbers[i] - bitCode[j]);
            }
        }
        currentMin = *min_element(cost[i].begin(), cost[i].end());
        currentMinIndex = find(cost[i].begin(), cost[i].end(), currentMin) - cost[i].begin();
        if (beforeMinIndex == currentMinIndex)
        {
            answer += "0";
        }
        else
        {
            answer += "1" + bitMap[bitCode[currentMinIndex]];
        }
        beforeMin = currentMin;
        beforeMinIndex = currentMinIndex;
    }

    // 출력
    // 실행 시간과 결과 값을 출력합니다.
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;

    cout << beforeMin << endl;
    cout << answer << endl;
    // cout << "실행시간: " << duration << "초" << endl;
} 