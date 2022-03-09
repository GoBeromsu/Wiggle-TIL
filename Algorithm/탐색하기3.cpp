#include <stdio.h>
#include <iostream>
#include <cmath>

using namespace std;

int findIndex(int data[], int n)
{
    // 문제에서는 평균과 가장 가까운 값을 찾으라 했지만, 연산이 모두 중복되기 때문에 합까지만 구하고 문제를 풀어도 이상 없다.
    int sum = 0;
    int x=0;
    for (int i = 0; i < n; i++)
        sum += data[i];

    // x는 현재 탐색한 값들 중 가장 평균과 가까운 거리에 위치한 인덱스
    // 순차적으로 x보다 더 평균과 가까운 값이 등장하면 x 값을 계속 업데이트 한다.
    for(int i=0;i<n;i++){
        int dx=abs(n*data[x]-sum);
        int di=abs(n*data[i]-sum);
        if(dx>di)
            x=i;
    }
    // 문제에서 데이터의 번호는 입력 받은 순서대로 1부터 시작한다 했으므로 +1 해야한다.
    // 인덱스는 0부터 시작하기 때문이다.
    return x+1;
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

    int answer = findIndex(data, n);
    printf("%d %d\n", answer,data[answer-1]);

    delete[] data;
    return 0;
}