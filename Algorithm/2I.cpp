#include <cstdio>
#include <iostream>

using namespace std;

// 배열이 연속적인지 확인하는 함수입니다.
bool isConsercutive(int data[], int n)
{
    //배열의 최댓 값과 최솟 값을 저장하는 변수를 선언합니다.
    int max_data = data[0];
    int min_data = data[0];
    // 배열을 탐색하며 최댓 값과 최솟 값을 찾습ㄴ미다.
    for (int i = 1; i < n; i++)
    {
        if (max_data < data[i])
            max_data = data[i];
        if (min_data > data[i])
            min_data = data[i];
    }
    // max_data-min_data가 n-1가 같다면 이 배열은 연속적입니다.
    // 그래서 위의 조건을 만족하는지 확인 후 값을 반환 합니다
    if (max_data - min_data == n - 1)
    {
        return true;
    }
    return false;
}

int main()
{
    int n;
    int *data;
    scanf("%d", &n);
    data = new int[n]; //크기가 n인 배열을 생성한다.

    for (int i = 0; i < n; i++) // 배열에 숫자를 입력합니다
    {
        scanf("%d", &data[i]);
    }
    // 배열이 연속적인 정수 수열로 표현 될 수 있는지 판단합니다
    bool result = isConsercutive(data, n);
    // result가 참일 경우 YES 아니면 NO를 출력합니다.
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