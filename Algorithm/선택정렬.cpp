#include <stdio.h>
#include <iostream>

int getMinIndexInRange(int data[], int n, int begin, int end)
{   
    // start부터 end까지에서 값이 가장 작은 인덱스를 탐색해서 반환한다
    int index = begin;
    for (int i = begin; i <= end; i++)
    {
        if (data[index] > data[i])
            index = i;
    }
    return index;
}

void selectionSort(int data[], int n)
{
    // 주어진 배열을 선형 탐색한다.
    for (int i = 0; i < n; i++)
    {   
        // 반복문이 1회 실행 될 때마다 하나씩 정렬된다.
        // minIndex는 i부터 n-1까지의 인덱스 중 가장 작은 값을 가지고 온다.
        int minIndex = getMinIndexInRange(data, n, i, n - 1);
        int temp = data[minIndex];
        data[minIndex] = data[i];
        data[i] = temp;
    }
    
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

    selectionSort(data, n);

    for (int i = 0; i < n; i++)
    {
        if (i > 0)
            printf(" ");
        printf("%d", data[i]);
    }

    delete[] data;
    return 0;
}