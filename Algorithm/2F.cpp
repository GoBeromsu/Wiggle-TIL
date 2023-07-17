#include <cstdio>
#include <cmath>
#include <climits>
#include <iostream>

using namespace std;

class Point2D
{
    // 클래스 내에서 쓰일 변수를 선언합니다
private:
    int x;
    int y;

public:
    // Point2D 생성자입니다.
    Point2D(int x = 0, int y = 0)
    {
        this->x = x;
        this->y = y;
    }

    // 2차원 평면 상에서 점 this부터 점 target까지 거리의 제곱을 계산하는 함수
    int getSquaredDistanceTo(const Point2D &target) const
    {
        // dx와 dy는 두 천체 간의 x좌표와 y 좌표 간의 차의 제곱입니다.
        // 두 점 간의 거리는 크기이므로 절댓값입니다.
        int dx = abs(this->x - target.x);
        int dy = abs(this->y - target.y);
        return (dx * dx) + (dy * dy);
    }
    // 두 천체 간의 거리를 구하고 반환하는 함수입니다.
    double getDistatanceTo(const Point2D &target) const
    {
        double sqd = (double)this->getSquaredDistanceTo(target);
        return sqrt(sqd);
    }
};

int main()
{
    int n;
    Point2D *points;
    // Point2D 배열을 선언하고 크기를 지정합니다.
    scanf("%d", &n);
    points = new Point2D[n];

    for (int i = 0; i < n; i++)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        // 선언한 배열에 순차적으로 x,y 좌표 값을 입력합니다.
        points[i] = Point2D(x, y);
    }
    // 가장 가까운 두 천체의 거리를 저장할 변수와 천체 쌍의 수를 저장할 변수를 선언합니다.
    int min_sqd = INT_MAX;
    int min_cnt = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            int sqd = points[i].getSquaredDistanceTo(points[j]);

            // 현재 sq가 최소 천체 쌍의 거리보다 작을 경우 최소 천체 쌍의 거리를 교체 합니다.
            // count도 다시 초기화합니다.
            // count를 초기화해도 되는 이유는 새로운 최소 천체 쌍의 거리는 전체 인덱스를 검사하던 중 처음 만났기 때문에 count는 1임이 자명합니다.
            if (sqd < min_sqd)
            {
                min_sqd = sqd;
                min_cnt = 1;
            }
            // 현재 최소 거리만큼 떨어진 천체를 만나면 카운트를 올림니다.
            else if (sqd == min_sqd)
            {
                min_cnt++;
            }
        }
    }
    // 최소 천체 쌍의 거리와 횟수를 출력합니다.
    double distance = sqrt(min_sqd);
    printf("%.1f\n", distance);
    printf("%d\n", min_cnt);

    delete[] points;
    return 0;
}