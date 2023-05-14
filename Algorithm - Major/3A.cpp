#include <cstdio>

using namespace std;

const int MAX_TABLE_LENGTH = 10000;

// 배열 테이블을 순차적으로 탐색하며 빈도수를 채웁니다.
void fillFrequencyTable(int data[], int n, int table[])
{
    for (int i = 0; i < n; i++)
    {
        table[data[i]] += 1;
    }
}

int getFrequentNumber(int data[], int n)
{

    int *table = new int[MAX_TABLE_LENGTH]; // 끝 네자리수 범위의 배열을 선언합니다.
    int frequent_count = 0;                 // 최대 빈도수를 저장하는 함수
    int frequent_number = 0;
    int current_count = 0;  // 현재 번호의 빈도수를 저장하는 변수
    int current_number = 0; // 현재 번호를 저장하는 변수

    fillFrequencyTable(data, n, table); //테이블에 입력 받은 변수의 빈도수를 저장한다.
    for (int i = 0; i < n; i++)
    {

        current_number = data[i];              // i번 째로 입력된 번호를 저장합니다.
        current_count = table[current_number]; // 현재 번호의 빈도수를 저장합니다.

        if (frequent_number != current_number) // 현재 번호와 최대 빈도 번호와 값이 같은지 비교한다
        {
            if (frequent_count < current_count) //두 번호가 다름이 자명하므로, 빈도수를 비교해 현재 번호의 빈도수가 최대 빈도수 보다 크다면
            {
                frequent_count = current_count; // 최대 빈도 번호와 빈도를 업데이트한다.
                frequent_number = current_number;
            }
            else if (frequent_count == current_count && frequent_number > current_number) // 사전 순으로 정렬하기 위해 빈도수는 같은데 누가 값이 더 큰지 확인한다.
            {
                frequent_number = current_number;
            }
        }
    }

    delete[] table;

    return frequent_number;
}

int main()
{
    int n;

    scanf("%d", &n); // 변수 n을 입력 받습니다.
    int *data = new int[n];

    for (int i = 0; i < n; i++) //배열 data에 번호를 저장합니다.
    {
        scanf("%d", &data[i]);
    }

    int answer = getFrequentNumber(data, n);

    printf("%0.4d", answer); // XXXX 형식으로 출력 Format을 맞춥니다.

    delete[] data;
    return 0;
}