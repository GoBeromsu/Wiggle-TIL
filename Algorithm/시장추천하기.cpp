#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    cin >> N;
    // 현재까지 최다득표한 후보들의 목록입니다.
    vector<string> curMaxFreqName;

    // 각 후보 이름과 득표 수를 저장하는 key-value Map
    map<string, int> frequencyMap;

    int maxFrequency = 0; // 가장 많은 득표수

    //각이름이하나추가될때마다 현재까지의 최다 특표 값 갱신, 최다 득표 후보 리스트를 갱신해간다.
    // vector의 clear메소드는 O(1)이다.
    for (int i = 0; i < N; i++)
    {
        string st;
        cin >> st;                // 이름을 입력 받습니다.
        frequencyMap[st]++;       //입력 받은 이름의 카운트를 올립니다.
        int k = frequencyMap[st]; // 이름의 카운트를 저장합니다.
        if (k > maxFrequency)     //최대 빈도수 보다 높다면
        {
            maxFrequency = k;       // maxFrequency로 지정한 후,
            curMaxFreqName.clear(); // 기존의 저장된 maximum 값들을 지웁니다.
            curMaxFreqName.push_back(st);
        }
        else if (k == maxFrequency) // 빈도수가 동일하다면, 추후 정렬을 위해 값을 넣어 둡니다.
        {
            curMaxFreqName.push_back(st);
        }
    }

    // 최대 득표 후보 수를 출력한다.
    cout << maxFrequency << endl;

    // 최대 득표를한 동점 후보들 이름을 사전순으로 출력한다.
    map<string, int>::iterator it;                                  // map iterator를 생성합니다.
    for (it = frequencyMap.begin(); it != frequencyMap.end(); it++) //순차적으로 iterator를 이동시킵니다.
    {                                                               // iterator의 경우, map에서 사용할 경우 key 값을 오름차순 정렬한다.
        if (it->second == maxFrequency)                             //빈도수가 최대  빈도수와 같다면 출력합니다.
        {
            printf("%s ", it->first.c_str()); // key 값인 이름을 출력합니다.
        }
    }
}