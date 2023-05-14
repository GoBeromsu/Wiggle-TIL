#include <iostream>
#include <cstdio>

using namespace std;
// 주어진 좌표의 겹쳐진 넓이는 구하는 함수입니다.
int get_area(int la, int ra, int ta, int ba, int lb, int rb, int tb, int bb)
{

    int l, r, t, b;
    l = max(la, lb); // left 좌표는 la와 lb의 최댓 값입니다.
    r = min(ra, rb); // right 좌표는 ra와 rb의 최솟 값입니다.
    t = min(ta, tb); // top 좌표는 ta와 tb의 최솟 값입니다.
    b = max(ba, bb); // bottom 좌표는 ba와 bb의 최댓 값입니다.

    //ㅣ이 r 보다 작은 경우, bottom이 top 보다 낮은 경우만 넓이가 겹친다
    if (l <= r && b <= t) //겹치는 면적이 0이 아닌 경우에만 넓이를 return 한다.
        return ((r - l) * (t - b));
    return 0;
}

void test_case()
{
    int ax, ay, bx, by;
    int px, py, qx, qy;
    scanf("%d %d %d %d", &ax, &ay, &bx, &by); // a와 b의 x,y 좌표를 입력 받는다.
    scanf("%d %d %d %d", &px, &py, &qx, &qy); // p와 q의 x,y 좌표를 입력 받는다.

    int la, ra, ba, ta; // 사각형 A의 left,right,bottom, top의 좌표를 나타낸다.
    la = min(ax, bx);
    ra = max(ax, bx);
    ta = max(ay, by);
    ba = min(ay, by);

    int lb, rb, bb, tb; // 사각형 B의 left,right,bottom, top의 좌표를 나타낸다.
    lb = min(px, qx);
    rb = max(px, qx);
    tb = max(py, qy);
    bb = min(py, qy);

    int answer = get_area(la, ra, ta, ba, lb, rb, tb, bb); // get_area에서 겹치는 넓이를 얻어온다.
    printf("%d\n", answer);
}

int main()
{
    int t;
    scanf("%d", &t); // testcase의 갯수를 입력 받는다.
    for (int i = 0; i < t; i++)
    { // 순차적으로 testcase를 실행한다.
        test_case();
    }
}