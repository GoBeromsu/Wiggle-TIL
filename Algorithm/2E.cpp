#include <cstdio>
#include <iostream>

using namespace std;

// 주어진 숫자가 소수인지 판별하는 함수
// return true 소수라면
// return false 소수가 아니라면
bool isPrime(int N)
{
    // 1은 소수가 아니기 때문에 N이 1이면 false를 반환한다
    if (N == 1)
    {
        return false;
    }
    // 소수를 탐색하는데 있어 1~N까지 탐색할 필요 없다.
    // n^0.5 이상 끼리의 곱은 N보다 크기 때문이다.
    // i*i가 N보다 작은지 확인함으로써 탐색 범위를 N^0.5로 줄일 수 있다.
    for (int i = 2; i*i <= N; i++)
    {   

        if (N % i == 0)
        {   
            //N%i ==0이면 나머지가 하나도 없다 즉 소수가 아니다.
            return false;
        }
    }
    // 반복문을 모두 통과했다면 N은 소수이다.
    return true;
}

// 테스트 케이스를 소수인지 판별하는 함수
void testcase(int caseIndex)
{
    // n 은 소수인지 판별해야할 수입니다.
    int n;
    scanf("%d", &n);

    // n이 소수인지 판별하여 result에 값을 저장합니다.
    bool result = isPrime(n);
    printf("Case #%d\n", caseIndex);

    // result가 참이라면 YES, 아니라면 NO를 출력합니다.
    if (result)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}

int main()
{
    int caseSize;
    // 테스트 케이스의 갯수를 입력 받습니다.
    scanf("%d\n", &caseSize);
    // 각각의 테스트 케이스의 입력을 받습니다.
    for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1)
    {
        testcase(caseIndex);
    }
}