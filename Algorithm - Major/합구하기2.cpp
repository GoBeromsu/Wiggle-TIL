#include <stdio.h>
#include <iostream>

using namespace std;

void solve(int data[], int n, int p, int q)
{
    // count : 무게 제한에 걸리지 않는 사람의 수를 카운트
    // sum : 탑승한 승객의 몸무게의 총합
    int count = 0;
    int sum = 0;

    // 저장된 승객들의 몸무게를 하나씩 불러와서 무게 제한에 걸리는지 확인한다
    for (int i = 0; i < n; i++)
    {
        if (data[i] <= p)
        {   
            // 무게 제한에 걸리지 않는 경우 count를 올리고 sum에 몸무게를 추가한다.
            sum += data[i];
            count++;
        }
    }
    printf("%d %d\n", count, sum);

    // 탑승한 승객 무게의 합이 인원 제한을 넘지 않았다면 YES 아닐시 NO 출력
    if (sum >= q)
    {
        printf("NO\n");
    }
    else
        printf("YES\n");
}
int main()
{
    int n, p, q;
    int *data;

    scanf("%d %d %d", &n, &p, &q);
    data = new int[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data[i]);
    }

    solve(data, n, p, q);

    delete[] data;
    return 0;
}