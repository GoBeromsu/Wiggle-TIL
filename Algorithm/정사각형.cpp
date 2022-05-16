#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;

class Point2D
{
public:
    int x;
    int y;
    int index;
    // 생성자로써, 인덱스와 x,y 좌표를 입력 받는다.
    Point2D(int index, int x, int y)
    {
        this->index = index;
        this->x = x;
        this->y = y;
    }
    // 생성자로써 x,y의 좌표를 입력 받는ㄷ다.
    Point2D(int x, int y)
    {
        this->index = 1;
        this->x = x;
        this->y = y;
    }

    long long getSquaredDistanceTo(Point2D target)
    {
        // 두 좌표간의 제곱거리를 계산하는 함수이다.
        long long dx = abs(this->x - target.x); // 가로의 길이를 구한다.
        long long dy = abs(this->y - target.y); // 세로의 길이를 구한다.
        return dx * dx + dy * dy;
    }

    double getDistanceTo(Point2D target)
    {
        // 두 좌표간의 실수 거리를 계산
        long long sqd = this->getSquaredDistanceTo(target);
        return sqrt(sqd);
    }

    bool operator<(const Point2D &other) const
    {
        // 각 좌표의 우선순위를 비교하기 위한 비교 연산자이다.

        // x좌표가 다르다면 x좌표를 기준으로 비교한다.
        if (this->x != other.x)
        {
            return this->x < other.x;
        }
        // x좌표가 같다면 y좌표를 기준으로 비교한다.
        return this->y < other.y;
    }
};

long long getMaximumSquareArea(int n, const vector<Point2D> &points)
{
    long long answer = 0;

    // 모든 점을 Set에 저장한다
    set<Point2D> pointSet;
    for (int i = 0; i < n; i += 1)
    {
        pointSet.insert(points[i]);
    }

    for (int i = 0; i < n; i += 1)
    {
        Point2D firstPoint = points[i]; // 순차적으로 점을 지정합니다.
        for (int j = 0; j < n; j += 1)
        {
            if (i == j)
            {
                continue; // 같은 값을 제외한다.
            }
            Point2D secondPoint = points[j]; //순차적으로 다른 점을 지정합니다.
            // 두 점 사이의 넓이를 구합니다.
            // 임의로 두 점 사이의 넓이를 구한 후, 나머지 두 점이 있는지 체크함으로써 연산을 줄일 수 있습니다.
            long long dimensions = firstPoint.getSquaredDistanceTo(secondPoint);
            if (dimensions < answer) // 임의로 두 점 사이의 넓이가 기존의 값 보다 작다면, 다음 회차 탐색을 시작합니다.
                continue;

            int dx = secondPoint.x - firstPoint.x; // 두 점의 가로 길이를 구합니다.
            int dy = secondPoint.y - firstPoint.y; // 두 점의 세로 길이를 구합니다.
                                                   // 벡터 <dx, dy>를 90도로 회전시키면 <-dy, dx>가 된다.
                                                   // 90도 회전 시킨 두 점은 정사각형을 구성하는 두 점이다.
            Point2D pd(firstPoint.x - dy, firstPoint.y + dx);
            Point2D pc(secondPoint.x - dy, secondPoint.y + dx);

            // 임의로 구한 두 점이 실제로 존재하는지 확인한 후 최댓 값을 확인합니다.
            if (pointSet.find(pc) != pointSet.end() && pointSet.find(pd) != pointSet.end())
            {
                answer = max(answer, dimensions);
            }
        }
    }

    return answer; // answer을 반환합니다.
}

void process(int caseIndex)
{
    int n;
    cin >> n; // 입력 받을 점의 갯수를 설정합니다.

    vector<Point2D> points;

    for (int i = 0; i < n; i += 1)
    {
        int x, y;
        cin >> x >> y;
        points.push_back(Point2D(i, x, y)); // 순차적으로 주어진 점들을 배열에 입력합니다.
    }

    double answer = getMaximumSquareArea(n, points); // 최대 넓이를 출력한다.

    cout << fixed << setprecision(2) << answer << endl; // 결과 값을 출력한다.
}

int main()
{
    int caseSize;
    cin >> caseSize; //테스트 케이스의 갯수를 입력 받는다.

    for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1)
    {
        process(caseIndex); // 테스트 케이스를 실행 시킨다.
    }
}