#include <stdio.h>

using namespace std;

int getElementTypeCount(int data[], int n)
{
    // 종류를 카운트할 변수 count와 이전 앨범의 값을 저장할 변수 bValue를 선언한다.
    // 정렬된 값이므로 순차적으로 탐색하며 이전 앨범의 값과 비교하여 다르면 count 하면 된다.
    int count = 1;
    int bValue = data[0];

    for (int i = 1; i < n; i++)
    {
        if (data[i] != bValue)
        {   
            // 현재 인덱스의 값이 이전 앨범의 값과 다르다면 다른 화보이다.
            // count하고 다음 탐색을 위하여 bValue를 현재 화보의 값으로 바꾼다
            count += 1;
            bValue = data[i];
        }
    }
    return count;
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

    int answer = getElementTypeCount(data, n);

    printf("%d\n", answer);

    delete[] data;
    return 0;
}