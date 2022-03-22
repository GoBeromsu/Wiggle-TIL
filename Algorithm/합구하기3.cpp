#include <stdio.h>
#include <iostream>

using namespace std;
int getRangeSumFromeOne(int i)
{   

    // 1부터 i까지의 합을 반환합니다.
    // 만약 숫자의 합을 여러 개 구해야한다면, 전역 변수를 선언해서 값을 미리 저장해두면 연산 속도를 올릴 수 있을 것이다.
    // for 문 실행 시킬 때 i 등을 자주 사용하는데, 매개 변수라 혼용하지 않도록 조심할 것
    int answer=0;
    for(int j=1;j<=i;j++){
        answer+=j;
    }
    return answer;
}

long long getAnswer(int N)
{
    long long answer = 0;
    // 1~i의 합을 값을 받아 그 것들을 다시 더해 i까지의 합을 구한다.
    for (int i = 1; i <= N; i++)
    {
        int rangesum = getRangeSumFromeOne(i);
        answer += rangesum;
    }
    return answer;
}

int main()
{
    int n;
    scanf("%d", &n);
    long long answer = getAnswer(n);
    printf("%lld\n", answer);

}