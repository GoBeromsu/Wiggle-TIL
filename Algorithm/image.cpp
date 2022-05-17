#include <iostream>
#include <vector>
#include <stdlib.h>
#include <map>
#include <time.h>
#include <string>
#include <algorithm>
#include <time.h>
using namespace std;

map<int, string> bitMap;            // level과 code를 매핑하는 일종의 딕셔너리 입니다.
int bitCode[4] = {1, 86, 172, 256}; // 연산의 편의를 위해 level을 저장해둔 배열입니다.
// level과 code를 맵핑합니다.
void makeMap()
{
    bitMap[1] = "00";
    bitMap[86] = "01";
    bitMap[172] = "10";
    bitMap[256] = "11";
}
int main()
{
    makeMap(); // bitMap을 생성합니다.
    //가중치와 숫자의 갯수를 입력 받습니다.
    int N = 0;
    int W = 0;
    cin >> N >> W;

    // 숫자를 순차적으로 입력 받습니다.
    vector<int> numbers(N, 0);
    for (int i = 0; i < N; i++)
    {
        cin >> numbers[i];
    }

    clock_t start;
    clock_t finish;
    double duration;
    start = clock();

    vector<vector<int>> cost(N);       //변환 비용을 저장할 2차원 정수 벡터입니다.
    vector<vector<string>> answers(N); //변화한 문자열을 저장할 2차원 문자열 벡터입니다
    vector<int> tempCost(4, 0);        // cost[i][j]에 들어갈 비용들을 고를 때 사용할 임시 벡터입니다.
    vector<string> tempAnswer(4);      // answer[i][j]에 들어갈 비용들을 고를 때 사용할 임시 벡터입니다.
    int minIdx = 0;                    // 최소 비용의 인덱스를 나타내는 변수입니다.
    int result = 0;                    //최소 변환 비용을 저장할 변수입니다.

    // cost와 answer를 초기화합니다.
    for (int i = 0; i < N; i++)
    {
        cost[i].resize(4, 0);
        answers[i].resize(4, "");
    }
    // cost와 answer에 들어갈 내용은 cost[i][j]가 되기 위한 최소 비용입니다.
    for (int i = 0; i < N; i++)
    {
        // 처음 탐색을 시작한 경우입니다.
        if (i == 0)
        {
            for (int j = 0; j < 4; j++)
            {
                // 가중치는 모두 동일하므로, 각자 level에 맞는 비트만 저장합니다.
                cost[i][j] = abs(numbers[i] - bitCode[j]) + 2 * W;
                answers[i][j] += bitMap[bitCode[j]];
            }
        }
        else
        {
            // 현재 문제는 DP 문제이므로 점화식은 아래와 같습니다.
            // cost[i] = cost[0~4] + W + numbers[i]-LEVEL[j]입니다.
            // 이전 회차의 비용들 + 가중치 + 오차가 최소인 값을 찾습니다.
            for (int j = 0; j < 4; j++)
            {
                for (int k = 0; k < 4; k++)
                {

                    tempCost[k] = cost[i - 1][k] + W + abs(numbers[i] - bitCode[j]); // 기본적으로 가중치 W는 최소한으로 가지므로 미리 더해줍니다
                    if (k != j)
                    {
                        tempCost[k] += 2 * W;                                               // 이전 회차와 인덱스가 다르므로 가중치를 더합니다.
                        tempAnswer[k] += answers[i - 1][k] + "1" + bitMap[bitCode[j]] + ""; // 똑같이 인덱스가 다르므로 문자열에 변화를 줍니다.
                    }
                    else
                    {
                        tempAnswer[k] += answers[i - 1][k] + "0"; // 인덱스가 같으므로 0을 추가합니다.
                    }
                }
                result = *min_element(tempCost.begin(), tempCost.end());                    // cost[i][j]에 들어갈 최소 비용입니다.
                minIdx = find(tempCost.begin(), tempCost.end(), result) - tempCost.begin(); //최소 비용의 인덱스가 가리키는 문자열을 찾기 위한 인덱습입니다.

                cost[i][j] = result;                // 최소 비용을 저장합니다.
                answers[i][j] = tempAnswer[minIdx]; //최소 비용일 때의 문자열을 저장합니다.

                tempAnswer.clear(); //다음 연산을 위해 임시 벡터 answer를 초기화합니다.
                tempAnswer.resize(4);
            }
        }
    }
    result = *min_element(cost[N - 1].begin(), cost[N - 1].end());                       //최종 최소 변환 비용을 찾습니다.
    minIdx = find(cost[N - 1].begin(), cost[N - 1].end(), result) - cost[N - 1].begin(); // 그 인덱스를 찾습니다.
                                                                                         // 출력
    // 실행 시간과 결과 값을 출력합니다.
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;

    cout << result << endl;
    cout << answers[N - 1][minIdx] << endl;
    cout << "실행시간: " << duration << "초" << endl;
}