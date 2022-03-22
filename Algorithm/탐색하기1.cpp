#include <stdio.h>
#include <iostream>

using namespace std;

int findIndex(int data[], int n, int m)
{
    // 받은 값들을 순회하며 m이 있는지 탐색을 한다.
    // 원하는 값을 찾을 경우 그 값의 인덱스를 바로 반환한다.
    // return 시 함수는 종료되기 때문에 m이 배열 안에 없다면 -1을 반환하면 된다. 
    for (int i = 0; i < n; i++)
    {
        if (data[i] == m)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int n, m;
    int *data;

    scanf("%d %d", &n, &m);
    data = new int[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data[i]);
    }

    int answer = findIndex(data, n, m);
    printf("%d\n", answer);

    delete[] data;
    return 0;
}