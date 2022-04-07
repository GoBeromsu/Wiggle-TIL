#include <cstdio>
#include <vector>

using namespace std;

const int MAX_N = 1000000;
vector<int> FIBONACCI_TABLE;

/**
 * 피보나치 수열의 1~n번째 항을 배열에 저장하여 반환해주는 함수
 * * 단, 항의 가장 뒤 8자리만을 저장한다.
 * @param n
 * @return fibo[i] := 피보나치 수열의 i번째 항
 */
vector<int> makeFibonacciTable(int n)
{
    const int MOD = 100000000;
    // 피보나치 배열을 미리 선언해준다.
    vector<int> ret(n + 1);
    ret[1] = 0;
    ret[2] = 1;

    // f(n)=f(n-1)+f(n-2)를 식으로 나타낸다.
    //  mod 연산으로 뒷자리 수만 출력할 수 있고, 더하기 연산이기에 값이 이상해질 염려는 하지 않아도 된다.
    for (int i = 3; i <= n; i++)
    {
        ret[i] = ret[i - 1] + ret[i - 2];
        ret[i] %= MOD;
    }
    return ret;
}

/**
 * 피보나치 수열의 n번째 항을 반환하는 함수
 * 단, 항의 가장 뒤 8자리만을 반환한다.
 * @param n
 * @return
 */
int getFibo(int n)
{
    //피보나치 테이블에서 원하는 값을 찾는다
    return FIBONACCI_TABLE[n];
}

int main()
{
    FIBONACCI_TABLE = makeFibonacciTable(MAX_N);
    // 테스트 ;케이스의 갯수를 입력 ;받는다.
    int caseSize;
    scanf("%d", &caseSize);

    for (int caseIndex = 1; caseIndex <= caseSize; ++caseIndex)
    {
        int n;
        scanf("%d", &n);

        // 피보나치 수열의 n번째 항을 계산하여 출력한다.
        int answer = getFibo(n);
        printf("%d\n", answer);
    }

    FIBONACCI_TABLE.clear();

    return 0;
}