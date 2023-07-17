#include <stdio.h>

using namespace std;

int getMaximumHeight(int height[], int month[], int n, int m)
{   
    // 최대 값을 저장하기 위한 변수 max를 선언한다.
    // 키는 0일 수 없기에 0으로 초기화한다.
    int max = 0;
    for (int i = 0; i < n; i++)
    {   
        // 현 인덱스가 생일인지 확인 후 참이면 현재 키의 최댓값과 비교 연산을 한다.
        if (month[i] == m && max < height[i])
        {
            // max가 현 인덱스의 키보다 작을 경우 max를 교체한다.
            max = height[i];
        }
    }
    // max가 초기 값과 동일한 경우 -1을 리턴한다
    if (max == 0)
    {
        return -1;
    }
    return max;
}

int main()
{
    int n, m;
    int *height;
    int *month;

    scanf("%d", &n);
    height = new int[n];
    month = new int[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &height[i]);
    }

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &month[i]);
    }

    scanf("%d", &m);

    int answer = getMaximumHeight(height, month, n, m);

    printf("%d", answer);

    delete[] height;
    delete[] month;
    return 0;
}