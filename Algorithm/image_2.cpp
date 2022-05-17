#include <iostream>
#include <vector>
#include <stdlib.h>
#include <map>
#include <time.h>
#include <string>
#include <algorithm>

using namespace std;
map<int, string> bitMap; //주어진 비트에 해당하는 코드를 맵핑하는 map입니다.
string answer;
// 이진 비트들의 level을 연산의 편의를 위해 선언해둡니다.
int bitCode[4] = {1, 86, 172, 256};

// 비트 코드 map을 정의합니다.
void makeMap()
{
    bitMap[1] = "00";
    bitMap[86] = "01";
    bitMap[172] = "10";
    bitMap[256] = "11";
}

void editAnswer(int bitCode, bool same)
{
    if (same)
    {
        answer += "0";
    }
    else
    {
        answer += "1" + bitMap[bitCode];
    }
}
vector<int> findMinNum(int number, int W, int beforeIdx)
{
    int currentError = 0;
    int minimumError = 9999999;
    int minimumIdx = 0;
    vector<int> result;
    for (int i = 0; i < 4; i++)
    {
        currentError = abs(number - bitCode[i]) + W;
        if (i != beforeIdx)
        {
            currentError += 2 * W;
        }
        if (minimumError > currentError)
        {
            minimumError = currentError;
            minimumIdx = i;
        }
        // cout << minimumIdx<<" " << currentError << endl;
    }
    result = {minimumIdx, minimumError};
    return result;
}
int main()
{
    //가중치와 숫자의 갯수를 입력 받습니다.
    int N = 0;
    int W = 0;
    cin >> N >> W;
    // N = 4;
    // W = 10;
    //  비트 코드 map을 정의합니다.
    makeMap();

    // 수열을 순차적으로 입력 받습니다.
    vector<int> numbers(N, 0);
    // numbers = { 100, 120, 140, 220 };
    for (int i = 0; i < N; i++)
    {
        cin >> numbers[i];
    }

    vector<int> cost(N, 0);
    int beforeIndex = 0;
    int currentIndex = 0;
    int currentError = 0;
    for (int i = 0; i < N; i++)
    {
        if (i == 0)
        {
            int mini = abs(numbers[0] - bitCode[0]);
            for (int j = 1; j < 4; j++)
            {
                if (mini > abs(numbers[i] - bitCode[j]))
                {
                    mini = abs(numbers[i] - bitCode[j]);
                    beforeIndex = j;
                }
            }
            cost[0] = mini + 2 * W;
            answer = bitMap[bitCode[beforeIndex]];
        }
        else
        {
            vector<int> minValue = findMinNum(numbers[i], W, beforeIndex);
            currentIndex = minValue[0];
            currentError = minValue[1];
            cost[i] = cost[i - 1] + currentError;
            if (currentIndex == beforeIndex)
            {
                editAnswer(bitCode[currentIndex], true);
            }
            else
            {
                editAnswer(bitCode[currentIndex], false);
            }
            beforeIndex = currentIndex;
        }
    }
    cout << cost[N - 1] << endl;
    cout << answer << endl;
}