#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

class City
{
public:
    int index;  // 도시의 인덱스
    int income; // 해당 도시의 소득

    // 도시의 인덱스와 수입을 저장합니다.
    City(int index, int income)
    {
        this->index = index;
        this->income = income;
    }
    // 오퍼레이션을 재정의하여 city의 소득을 비교하도록 합니다.
    bool operator<(const City &o) const
    {
        return this->income < o.income;
    }
    // 오퍼레이션을 재정의하여 city의 소득을 비교하도록 합니다.
    bool operator>(const City &o) const
    {
        return this->income > o.income;
    }
};

int getMaximumRangeDifference(int n, int k, const vector<City> &cities)
{

    // 최대 소득 차를 저자할 변수를 선언합니다.
    int answer = 0;

    // 소득이 가장 작은 도시부터 pop되는 우선순위 큐
    priority_queue<City, vector<City>, greater<City>> rangeMinimum;

    // 소득이 가장 높은 도시부터 pop되는 우선순위 큐
    priority_queue<City> rangeMaximum;
    // max와 min 큐에 도시들을 저장합니다.
    for (int i = 0; i < k - 1; i++)
    {
        rangeMaximum.push(cities[i]);
        rangeMinimum.push(cities[i]);
    }

    for (int i = k - 1; i < n; i++)
    {
        //우선 순위 큐에서 자동으로 도시 소득의 최대와 최솟값을 구한다.
        rangeMaximum.push(cities[i]);
        rangeMinimum.push(cities[i]);
        //현재 탐색하는 부분의 인덱스가 아닌 경우 그 값을 제거합니다.
        while (rangeMaximum.top().index < i - k + 1)
            rangeMaximum.pop();
        while (rangeMinimum.top().index < i - k + 1)
            rangeMinimum.pop();
        // 이전 소득 차와 계속 비교를 하여 최대 소득 차를 구한다.
        answer = max(answer, rangeMaximum.top().income - rangeMinimum.top().income);
    }

    return answer;
}

void process(int caseIndex)
{

    // 도시의 수와 연속되는 도시의 수를 입력 받습니다.
    int n, k;
    cin >> n >> k;
    vector<City> cities; // 도시들의 정보를 저장할 벡터를 선언한다.

    for (int i = 0; i < n; i += 1)
    {
        // 도시의 인덱스와 수입을 입력 받아 저장합니다.
        int income;
        cin >> income;
        cities.push_back(City(i, income));
    }
    // 도시 간 소득의 최댓 값을 저장합니다.
    int answer = getMaximumRangeDifference(n, k, cities);
    // 닶을 출력합니다.
    cout << answer << endl;
}

int main()
{
    // 테스트 케이스의 갯수를 입력 받습니다.
    int caseSize;
    cin >> caseSize;

    // 순차적으로 각 케이스를 실행합니다.
    for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1)
    {
        process(caseIndex);
    }
}