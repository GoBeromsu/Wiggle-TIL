#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#pragma warning(disable : 4996)
using namespace std;

class Player
{
public:
    int index;

    Player(int index = 0)
    {
        this->index = index;
    }
};

/**
 * 조세퍼스 게임을 수행하여 각 플레이어가 제거된 순서를 리스트로 반환하는 함수
 *
 * @param n         플레이어의 수
 * @param m         매 턴마다 건너 뛸 사람의 수
 * @param players   좌석에 앉아있는 순서대로 주어지는 플레이어 정보
 * @return
 */
vector<Player> getDeadPlayersList(int n, int m, const vector<Player> &players)
{
    // 현재 게임에서 제외된 플레이어들의 리스트
    vector<Player> deadPlayers;

    // 아직 게임에서 제외되지 않는 플레이어들의 리스트
    queue<Player> playerQueue;
    // 풀래이어들을 순차적으로 입력한다.
    for (int i = 0; i < n; i += 1)
    {
        playerQueue.push(players[i]);
    }

    // index는 제외할 사람의 순서이다. 즉 원형에서 m 번째 사람을 의미한다.
    int index = m;
    for (int i = 0; i < n; i++)
    {
        // 테이블이 원형이므로 m-1명을 건너뛰어야 m번째가 된다.
        index = 1 + (m - 1) % playerQueue.size();
        for (int j = 0; j < index - 1; j++)
        {
            // 순차적으로 m 번째까 될 때까지 테이블을 회전 시킨다.
            Player p = playerQueue.front();
            playerQueue.pop();
            playerQueue.push(p);
        }
        // m 번째 사람은 게임에서 제외한다.
        Player e = playerQueue.front();
        playerQueue.pop();
        // 제외 대상자를 리스트에 추가한다.
        deadPlayers.push_back(e);
    }
    return deadPlayers;
}

void testcase(int caseIindex)
{
    int n, m; // n과 m을 입력 받는다.
    scanf("%d %d", &n, &m);

    vector<Player> players; //플레이어들을 저장할 player 벡터를 선언한다.
    for (int i = 0; i < n; i++)
    {
        players.push_back(Player(i + 1)); // 1~n까지 player들의 인덱스를 지정한다.
    }
    // 제외되는 플레이어의 순서를 구한다.
    vector<Player> deadPlayers = getDeadPlayersList(n, m, players);

    // 제외되는 순서에 따라 플레이어를 출력한다.
    for (int i = 0; i < n; i++)
    {
        if (i > 0)
        {
            printf(" ");
        }
        // 제외된 플레이러를 지정한다.
        Player p = deadPlayers[i];
        printf("%d", p.index);
    }
    // 다음 케이스를 위해 줄을 바꾼다
    printf("\n");
}

int main()
{
    int caseSize;           //테스트의 케이스의 갯수를 저장할 변수를 선언한다.
    scanf("%d", &caseSize); // 테스트 케이스의 갯수를 저장한다.
                            // 테스트 케이스를 실행한다.
    for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1)
    {
        testcase(caseIndex);
    }

    return 0;
}
