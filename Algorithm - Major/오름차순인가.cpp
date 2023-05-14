#include <stdio.h>

using namespace std;

bool isOrdered(int data[], int n)
{   
    // 이전 인덱스의 값을 저장할 변수를 선언하고, data의 첫 인덱스 값을 저장한다.
    int beforeValue = data[0];
    // 탐색 범위는 beforValue 덕에 첫 인덱스는 탐색한 것이나 마찬가지여서, 1~n-1까지로 한다
    for (int i = 1; i < n; i++)
    {   
        //배열 data를 순차적으로 탐색하며, 현재 인덱스의 값이 이전 인덱스의 값보다 큰지 확인한다
        if (beforeValue >= data[i])
        {   
            // 현재 인덱스 값이 이전 값보다 작거나 같을 경우 탐색을 멈추고 false를 반환한다
            return false;
        }
        else
        {
            // 다음 인덱스를 탐색하기 위해 현재 인덱스를 beforeValue에 저장한다
            beforeValue = data[i];
        }
    }
    // 탐색 결과 오름차 순이라면 true를 반환한다
    return true;
}

int main()
{
    int n;
    int *data;

    scanf("%d", &n);
    data = new int[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data[i]);
    }

    bool result = isOrdered(data, n);

    if (result)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }
    delete[] data;
    return 0;
}