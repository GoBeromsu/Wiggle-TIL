#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <time.h>

using namespace std;
vector<bool> visited;//현재 방문한 인덱스를 체크할 벡터
set<vector<bool>> myset;//제재 이용자 선정 case(visited 벡터)들을 저장하고, 반복되는 case를 제거하는 집합입니다.

// 인자로 게임 이용자와 제한된 이용자의 ID의 길이를 정수로 입력 받아
// 길이가 같은지 다른지 확인하는 함수입니다.
bool checkSize(int idSize, int userSize)
{
    if (idSize == userSize)
        return true;
    else
        return false;
}
// 제재 이용자와 게임 이용자의 문자를 하나씩 매칭하며 제재 이용자가 될 가능성이 있는 이용자를 구분합니다.
bool checkEqual(int idSize, string restrictId, string userId)
{
    for (int i = 0; i < idSize; i++)
    {
        // *가 있는 경우 모든 문자열이 통과할 수 있으므로 예외처리를 합니다.
        if (restrictId[i] == '*')
        {
            continue;
        }
        else if (restrictId[i] != userId[i])
        {
            // 하나라도 다른 문자가 나타날 경우 바로 false를 리턴합니다.
            return false;
        }
    }
    // 모든 조건문을 통과했다면 제재 이용자가 될 가능성이 있는 ID이므로 true를 리턴합니다.
    return true;
}

// rID에는 제재 이용자가 될 가능성이 있는 유저들의 인덱스가 저장되어 있고
// v는 방문할 인덱스입니다.
// N 명 중 m 명만 제재 이용자가 될 수 있으므로, m은 dfs의 재귀를 끝낼 basecase의 역할도 합니다.
// count는 dfs가 몇 번 째 재귀를 하고 있는지 알려줍니다.
// dfs 1회 반복 때마다 1명씩 제재 이용자가 설정됩니다.(visited가 true인 경우)
void dfs(vector<vector<int>> rID, int v, int m, int count)
{

    visited[v] = true;  // v를 방문했으므로 체크합니다.
    if (m == count + 1) // m이 count+1이면 제재 이용자가 모두 나왔으므로 재귀를 마침니다.
    {

        // 집합 연산에 값을 넣을 경우 중복된 케이스를 제거하기에 myset에 visited 벡터를 넣습니다.
        // dfs를 써서 bruteforce 방식보다는 중복 연산을 줄였지만,
        // 한 이용자가 제재 아이디 2개가 될 가능성을 지니고 있을 경우 중복 연산이 발생한다.
        // 이를 막기 위해 집합을 이용하였다(집합에는 원소 중복을 제거하기 용이하다)
        myset.insert(visited);
        return;
    }
    // 메인 함수에서 dfs를 실행 시키는 반복문에서 초기 값이 rID[0]이였습니다.
    // 그리고 count도 0이었습니다. 
    // 즉 count를 1씩 더하며 재귀할 경우, 벡터 rID의 다음 인덱스의 값을 탐색하는데 사용할 수 있습니다.
    // 제재 이용자의 수만큼 반복하며,count를 1씩 더하며 재귀함으로써 다음 인덱스 탐색까지 진행합니다.
    for (int i = 0; i < rID[count + 1].size(); i++)//다음 제재 ID가 될 가능성이 있는 사용자들을 순차적으로 탐색합니다.
    {
        // 아직 i번째 제재 가능성있는 사용자를 체크하지 않았을 경우, 통과합니다.
        if (visited[rID[count + 1][i]] == false)
        {
            // 즉 다음 제재 이용자는 i번째 사용자 ID로 정해집니다.
            dfs(rID, rID[count + 1][i], m, count + 1);
            // 전역변수로 visited가 선언 되어 있기 때문에, 다음 반복을 위해 다시 false로 값을 돌려 놓습니다.
            visited[rID[count + 1][i]] = false;
        }
    }
}

int main()
{

    int N = 0;         //게임을 이용하는 이용자 수
    vector<string> ID; //이용자 ID
    int m = 0;         //제제 대상자의 수
    vector<string> k;  //제재 대상자의 ID

    string id;  // 임시로 이용자 ID를 입력 받는 변수
    string kid; // 임시로 제재 대상자 ID 입력 받는 변수
    // N,m,ID,k를 순차적으로 입력 받는다.
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        cin >> id;
        ID.push_back(id);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        cin >> kid;
        k.push_back(kid);
    }

    // 실행 시간 계산에 쓰일 변수를 선언한다.
    clock_t start, finish;
    double duration;

    vector<vector<int>> rID; //제재 가능성 있는 ID들의 인덱스를 저장할 벡터
    vector<int> perID;       // rID에 넣을 인덱스들을 모아 놓는 벡터
    int idSize = 0;          // 가독성을 위해 제재 이용자 아이디의 길이를 임시로 저장하는 변수

    visited.resize(N, false); //방문한 곳을 확인할 벡터 visited를 초기화합니다.

    start = clock();

    // 제재 대상자의 ID를 탐색할 반복문입니다.
    for (int i = 0; i < m; i++)
    {
        idSize = k[i].size(); //제재 대상자의 id 길이입니다.
        perID.clear();        //다음 ID 정보를 저장하기 위해 초기화해줍니다.
        // ID 중 제재 가능성이 있는 ID를 탐색하는 반복문입니다.
        for (int j = 0; j < N; j++)
        {

            // 현재 인덱스의 이용자와 제재 이용자 ID의 길이가 같고,
            // 이용자와 제재 이용자 ID가 일치한다면 조건문을 통과합니다.
            if (checkSize(idSize, ID[j].size()) && checkEqual(idSize, k[i], ID[j]))
            {

                //우리가 궁금한 것은 인덱스 i 번째 제재 이용자와 겹치는 게임 이용자들의 인덱스입니다.
                // 위의 조건문을 모두 통과했다면 N[j]의 게임 이용자의 인덱스 j를 저장합니다.
                perID.push_back(j);
            }
        }
        // i 번째 제재 이용자와 겹치는 이용자들의 인덱스를 저장한 벡터를 rID에 순차적으로 PUSH합니다.
        rID.push_back(perID);
    }


    // dfs 함수의 초기 값으로 rID[0] 즉 입력된 제재 이용자들 중 첫 번째 ID의 인덱스들을 순차적으로 넣습니다.
    for (int i = 0; i < rID[0].size(); i++)
    {
        dfs(rID, rID[0][i], m, 0);
        fill(visited.begin(), visited.end(), false);// 앞서 dfs 연산이 끝났으니 다음 반복을 위해 visited를 초기화 해줍니다.
    }
    // 출력
    // 실행 시간과 결과 값을 출력합니다.
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    cout << myset.size() << endl;//myset의 크기는 경우의 수와 같으므로 myset의 사이즈를 출력하면 정답입니다.
    cout << "실행시간: " << duration << "초" << endl;

    return 0;
}