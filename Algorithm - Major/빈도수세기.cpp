#include <stdio.h>
#include <map>
using namespace std;

int main()
{
    int n; //입력 받을 숫자의 갯수를 저장할 변수입니다.
    scanf("%d", &n);
    map<int, int> frequencyMap; //빈도수를 저장할 map입니다.
    for (int i = 1; i <= n; i++)// 순차적으로 숫자를 입력 받습니다.
    {
        int x;// 입력 받을 값을 저장할 변수 입니다.
        scanf("%d", &x);
        frequencyMap[x]++;//입력 받은 숫자의 카운트를 올립니다.
        printf("%d %d\n", frequencyMap.size(), frequencyMap[x]);//입력 받은 숫자들의 빈도수를 순차적으로 출력합니다.
    }
    return 0;
}