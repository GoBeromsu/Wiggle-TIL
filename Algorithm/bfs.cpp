#include <iostream>
#include <queue>

using namespace std;

int map[10][10] = {0}; //각 노드들과 이어진 노드를 저장할 2차원 배열
int visit[10] = {0};   // 계산의 용이함을 위해 0번 인덱스를 사용하지 않을 것임으로 0을 추가해둡니다.

queue<int> q; // 노드들을 넣을 큐를 만듭니다.

int num, edge_num; // 노드와 엣지의 갯수를 저장할 변수입니다.

void bfs(int v)
{
    cout << v << "\n"; // 방문한 노드를 출력합니다.
    q.push(v);         // 큐에 노드를 넣습니다.
    while (!q.empty()) //큐가 빌 때까지 계속 연산을 합니다 - 왜냐하면 bfs는 level 별로 순차적으로 진행하기 때문입니다.
    {
        int node = q.front(); //현재 큐의 제일 앞에 있는 노드입니다.
        q.pop();              //처음 while 문이 돌면 노드가 하나니까, 실제 연산 시작 전에 비워 줍니다.
                              // 위에 설명했다시피 level 별로 순차적으로 탐색을 하기 위함입니다.
        for (int i = 0; i < num; i++)
        {
            if (map[node][i] == 1 && visit[i] == 0) //현재 노드와 연결된 노드를 아직 방문하지 않았다면 방문합니다.
            {
                visit[node] = 1;   //다음 노드를 간 곳으로 체크합니다.
                cout << i << "\n"; // 다음 노드를 출력합니다.
                q.push(i);         // 큐에 다음 목적지를 넣습니다.
            }
        }
    }
}

int main()
{
    cin >> num >> edge_num; // 입력 받을 노드와 엣지들의 갯수를 입력 받습니다.
    for (int i = 0; i < edge_num; i++)
    {
        int v1, v2; //연결된 두 노드를 입력 받습니다.
        cin >> v1 >> v2;
        map[v1][v2] = map[v2][1] = 1; //연결된 노드들의 정보를 각자 map에 저장합니다.
    }
    bfs(1); // 탐색을 시작합니다.

    return 0;
}
