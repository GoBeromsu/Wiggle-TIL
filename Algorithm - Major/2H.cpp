#include <cstdio>
#include <iostream>

// 왼쪽 아래 좌표가 x,y인 픽셀이 반지름 R인 원에 포함되는가?
// 포함된다면 true, else false
bool isInside(long long x, long long y, long long R)
{
    // x^2+y^2<R^2를 만족해야함
    long long sqd = x * x + y * y;
    // 좌표 x,y가 원 안에 있는지 확인하고 참이면 true 아니면 false를 출력합니다. 
    if (sqd < R * R)
        return true;
    return false;
}

void testcase(int caseIndex)
{
    long long R;
    scanf("%lld", &R);

    long long sum = 0; // 1사분면에 존재하는 총 픽셀의 수
    long long y = R;
    for (long x = 0; x <= R; x++)
    {
        long long height = 0;
        for (; y >= 0; y--)
        {
            // 픽셀이 안에 있는지 확인한다
            if (isInside(x, y, R))
            //위에서 부터 내려오다가
            // 가장 최소로 원 안에 포함된 픽셀 (x,y) 그룹의 높이는 (y+1)이 된다.
            {
                height = (y + 1);
                break;
            }
        }
        sum += height; //너비는 1이므로 높이만 더하면 된다.
    }

    printf("#%d\n", caseIndex);
    
    printf("%lld\n", sum * 4);//한 사분면 내의 픽셀의 수를 찾았으니 곱하기 4해서 답을 출력합니다.
}

int main()
{
    int caseSize;
    scanf("%d", &caseSize);

    for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1)
    {
        testcase(caseIndex);
    }

    return 0;
}