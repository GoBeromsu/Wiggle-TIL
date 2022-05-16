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
    string answer = ""; // 코드를 저장할 문자열을 선언합니다.

    // 최소 에러 값을 찾자!

    vector<vector<int>> error(N);
    // 이중 벡터의 각 크기를 주어진  레벨의 갯수만큼으로 초기화 합니다.
    for (int i = 0; i < N; i++)
    {
        error[i].resize(4, 0);
    }
    int currentMin = 0;
    int currentMinIndex = 0;
    int beforeMinIndex = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            error[i][j] = abs(numbers[i] - bitCode[j]);
            if (i != 0)
            {

                error[i][j] += *min_element(error[i - 1].begin(), error[i - 1].end());
            }
        }

        currentMin = *min_element(error[i].begin(), error[i].end());
        currentMinIndex = find(error[i].begin(), error[i].end(), currentMin) - error[i].begin();

        if (i == 0)
        {
            answer += bitMap[bitCode[currentMinIndex]];
        }
        else if (currentMinIndex == beforeMinIndex)
        {
            answer += "0";
        }
        else
        {
            answer += "1" + bitMap[bitCode[currentMinIndex]];
        }
        beforeMinIndex = currentMinIndex;
    }
    cout << answer << endl;
    cout << *min_element(error[N - 1].begin(), error[N - 1].end()) + W * answer.length() << endl;

    for (int i = 0; i < error.size(); i++)
    {
        for (int j = 0; j < error[i].size(); j++)
        {
            cout << error[i][j] << " ";
        }
        cout << endl;
    }
}