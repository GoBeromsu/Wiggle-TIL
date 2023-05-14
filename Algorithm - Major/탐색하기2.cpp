#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

void printIndexes(string school[], int n)
{
    int first = -1;
    int last = -1;
    for (int i = 0; i < n; i++)
    {   
        // 저장된 학교 이름이 AJOU인지 확인한다.
        if (school[i] == "AJOU")
        {   
            // AJOU 대학교 학생을 처음 만날 경우에만 first의 인덱스를 해당 학생으로 바꾼다.
            if (first == -1)
            {
                first = i;
            }

            last = i;
        }
    }
    printf("%d %d\n", first + 1, last + 1);
}

int main()
{
    int n;
    char buff[11];
    string *school;

    scanf("%d", &n);
    school = new string[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%s", buff);
        school[i] = buff;
    }
    printIndexes(school, n);

    delete[] school;
    return 0;
}