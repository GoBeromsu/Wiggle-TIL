#include <stdio.h>
#include <vector>

using namespace std;

int process(int N, int m, std::vector<int> timeCount)
{
    int person = N;
    int time;
    vector<int> currentTime(m, 0);

    while (person > 0)
    {
        // 순환하면서 값을 올려줄 코드
        // 순환하면서 값이 max인 것들은 다시 초기화 하는거임
        person--;
    }
}

int main()
{
    // 초를 세는 count를 하나 만들어라!
    // 값을 어떻게 넣을건데???
    // 동적으로 초들을 채워야지
    // 배열을 두 개 선언해서 하나는 정보만 저장하고, 나머지는 카운트를 세가는거임
    // 그래서 매 반복할 때마다 1초씩 올리고 빈 곳이 있는지 확인하는거지
    // 비었으면 전체 사람의 수를 줄이고 다시 값을 초기화하는거야 캬 오졌다.

    int N, m = 0;
    vector<int> testTime;

    scanf("%d\n", &N);
    scanf("%d\n", &m);

    testTime.clear();
    testTime.resize(m, 0);

    int t = 0;

    for (int i = 0; i < m; i++)
    {
        scanf("%d", t);
        testTime.push_back(t);
    }

    process(N, m, testTime);

    return 0;
}