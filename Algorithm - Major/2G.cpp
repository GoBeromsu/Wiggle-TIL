#include <cstdio>
#include <iostream>

using namespace std;

void bubbleSort(int data[], int n)
{
    for (int i = 0; i < n; i++)
    {
        // n-1까지 탐색하는데 이전 탐색에서 확인한 부분은 제합니다.
        // negativecount를 통해 이미 정렬되었느지 확인합니다.
        int negativecount = 0;
        for (int j = 0; j < n - 1 - i; j++)
        {
            // 오름차순을 부정하는 쌍이 나오면 2개의 값의 자리를 교환합니다.
            if (data[j] > data[j + 1])
            {
                // temp에 data[j+1] 값을 임시로 저장하고 두 값을 바꿉니다
                int temp = data[j + 1];
                data[j + 1] = data[j];
                data[j] = temp;
                negativecount++;
            }
        }
        // negativecount가 0이라면 이미 정렬된 함수 이므로 멈춥니다
        if (negativecount == 0)
            break;
    }
}

int main()
{
    int n;
    int *data;

    // 숫자를 담을 배열 data를 선언합니다.
    scanf("%d", &n);
    data = new int[n];

    // 배열 data에 숫자를 입력합니다.
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data[i]);
    }
    bubbleSort(data, n);

    // 정렬된 배열 data를 출력합니다.
    for (int i = 0; i < n; i++)
    {
        if (i > 0)
        {
            printf(" ");
        }
        printf("%d", data[i]);
    }
    delete[] data;
    return 0;
}