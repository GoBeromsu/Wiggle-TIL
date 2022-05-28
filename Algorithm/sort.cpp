#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <time.h>
#include <algorithm>
#include <map>
using namespace std;
int answer = 0;
map<int, int> currentIndex;
vector<int> number(10, 0);

void print(vector<int> number)
{
    for (int i = 0; i < number.size(); i++)
    {
        cout << number[i] << " ";
    }
    cout << endl;
}
void update(int start, int K, vector<int> number)
{
    for (int i = start; i < start + K; i++)
    {
        currentIndex[number[i]] = i;
    }
}

int process(vector<int> number, int N, int K)
{
    for (int i = 0; i < number.size(); i++)
    {
        currentIndex[number[i]] = i;
    }

    for (int i = N; i > 0; i--)
    {
        while (1)
        {
            // cout << currentIndex[i];
            if (currentIndex[i] == i - 1) //자기 위치에 있는 경우
            {
                break;
            }
            if (currentIndex[i] + K > i) // k씩 옮긴다고 해서 옮기면 옮기지 못하는 경우
            {
                return -1;
            }
            else
            {
                int *a = &number[0];
                int updateIndex = currentIndex[i];

                sort(a + currentIndex[i], a + currentIndex[i] + K);
                update(currentIndex[i], K, number);
                print(number);
            }
            answer += 1;
        }
    }

    return answer;
}

int main()
{
    int N, K = 0;
    scanf("%d %d", &N, &K);
    // N = 3;
    // K = 3;
    number.resize(N, 0);
    // number = { 1,3,2 };
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &number[i]);
    }
    clock_t start, finish;
    double duration;
    start = clock();

    printf("%d\n", process(number, N, K));
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    cout << "실행시간: " << duration << "초" << endl;
}
