#include <cstdio>
#include <vector>

using namespace std;

const int MAX_SEAT_NUMBER = 1000;
const int MAX_COLOR_NUMBER = 100;

class Painting
{
public:
    int left;
    int right;
    int color;
    Painting(){};

    // Painting 객체 내의 변수들과 생성자를 선언한다.
    Painting(int left, int right, int color)
    {
        this->left = left;
        this->right = right;
        this->color = color;
    }
};

// 등장한 번호들에 대한 빈도수 테이블을 채우는 함수
/**
 * data[0] ~ data[n-1]에 등장한 번호들에 대한 빈도수 테이블을 채우는 함수
 * @param data
 * @param n
 * @param table  table[x] := data배열에서 x가 등장한 횟수
 */
void fillFrequencyTable(int data[], int n, int table[])
{
    // 배열 data를 순회하며 테이블의 빈도수를 하나씩 더해간다.
    for (int i = 0; i < n; i++)
    {
        table[data[i]] += 1;
    }
}

/**
 *
 * @param n : 좌석의 수. 좌석은 0~(n-1)번의 번호를 가진다.
 * @param m : 좌석을 칠한 횟수.
 * @param paintings  : 좌석들을 색칠한 이벤트들의 정보
 */
void solve(int n, int m, const Painting *paintings)
{
    int *seats = new int[n];
    for (int i = 0; i < n; i++)
    {
        seats[i] = 0; //처음 좌석은 전부 0으로 칠해져 있다
    }

    // 색깔의 수만큼 좌석을 순회하면서 색칠을 해갑니다.
    for (int i = 0; i < m; i++)
    {
        const Painting &p = paintings[i];
        for (int j = p.left; j < p.right + 1; j++)
        {
            seats[j] = p.color;
        }
    }

    int *table = new int[MAX_COLOR_NUMBER]; //숫자들의 빈도를 저장하는 테이블 선언
    for (int i = 0; i < n; i++)
    {
        table[i] = 0; //처음 빈도수는 전부 0으로 칠해져 있다
    }

    fillFrequencyTable(seats, n, table);
    int minColor = seats[0]; // 가장 적게 등장한 색상
    int maxColor = seats[0]; //가장 많이 등장한 색상
    for (int i = 1; i < n; i++)
    {
        // 최대와 최소 빈도수를 구할 때 분리해서 조건문을 작성해야한다.
        // max Color 의 값을 테이블을 순회하며 탐색한다.
        if (table[seats[i]] > table[maxColor])
        {
            maxColor = seats[i];
        }
        else if (table[seats[i]] == table[maxColor] && seats[i] < maxColor)
        {
            maxColor = seats[i];
        }
        // min Color 의 값을 테이블을 순회하며 탐색한다.
        if (table[seats[i]] < table[minColor])
        {
            minColor = seats[i];
        }
        else if (table[seats[i]] == table[minColor] && seats[i] < minColor)
        {
            minColor = seats[i];
        }
    }

    // 제일 많이 등장한 색상과 적게 등장한 색상을 출력한다.
    printf("%d\n", maxColor);
    printf("%d\n", minColor);

    delete[] seats;
}

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    // paintings[i]:= i번째에 일어난 색칠 이벤트의 정보
    Painting *paintings = new Painting[n];

    for (int i = 0; i < m; ++i)
    {
        scanf("%d", &paintings[i].left);
        scanf("%d", &paintings[i].right);
        scanf("%d", &paintings[i].color);

        // 좌석의 번호는 1번부터 시작하므로, 0 ~ (n-1) 범위를 맞추기 위해 1씩 빼준다.
        paintings[i].left -= 1;
        paintings[i].right -= 1;
    }
    // 문제의 답을 출력한다.
    solve(n, m, paintings);

    return 0;
}