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

int findUnder(int n)
{
    int num = 0;

    for (int i = 0; i < 4; i++)
    {
        if (bitCode[i] <= n)
        {
            num = i;
        }
    }
    return num;
}
bool checkMinIndex(int idx, int minIndex)
{
    if (idx == minIndex)
    {
        return true;
    }
    return false;
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

    int upper, under;
    int upperError, underError;
    int beforMinIndex = 0;
    int currentMin = 0;
    vector<int> cost(N, 0);
    for (int i = 0; i < N; i++)
    {
        under = findUnder(numbers[i]);
        upper = under + 1;
        upperError = abs(numbers[i] - bitCode[upper]);
        underError = abs(numbers[i] - bitCode[under]);
        cout << "범위 " << bitCode[under] << " - " << numbers[i] << " - " << bitCode[upper] << endl;

        if (i == 0)
        {
            if (upperError < underError)
            {
                beforMinIndex = upper;
            }
            else
            {
                beforMinIndex = under;
            }
            cost[i] = 2 * W + abs(numbers[i] - bitCode[beforMinIndex]);
            answer += bitMap[bitCode[beforMinIndex]];
        }
        else
        {
            if (checkMinIndex(under, beforMinIndex))
            {
                underError += W;
                upperError += 3 * W;
                if (underError <= upperError)
                {
                    cost[i] = underError;
                    beforMinIndex = under;
                    editAnswer(0, true);
                }
                else
                {
                    cost[i] = upperError;
                    beforMinIndex = upper;
                    editAnswer(bitCode[upper], false);
                }
            }
            else
            {
                underError += 3 * W;
                upperError += W;
                if (underError >= upperError)
                {
                    cost[i] = underError;
                    beforMinIndex = under;
                    editAnswer(bitCode[under], false);
                }
                else
                {
                    beforMinIndex = upper;
                    cost[i] = upperError;
                    editAnswer(0, true);
                }
            }
            cost[i] += cost[i - 1];
        }

        // cout << i << " 회차 : cost -" << cost[i] << " "
        //<< "문자 - " << answer << " " << endl;
        // cout << endl;
    }
    cout << cost[N - 1] << endl;
    cout << answer << endl;
}