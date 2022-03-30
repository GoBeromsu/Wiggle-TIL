#include <cstdio>

using namespace std;

const int MAX_TABLE_LENGTH = 10000;

// 
void fillFrequencyTable(int data[], int n, int table[])
{
    for (int i = 0; i < n; i++)
    {
        table[data[i]] += 1;
    }
}

int getFrequentNumber(int data[], int n)
{
    int frequent_number = 0;
    int *table = new int[MAX_TABLE_LENGTH];
    int max_count = 0;
    int current_count = 0;
    int current_number = 0;

    fillFrequencyTable(data, n, table);
    for (int i = 0; i < n; i++)
    {
        current_number = data[i];
        current_count = table[current_number];
        if (current_count > max_count)
        {
            frequent_number = current_number;
        }
        else if (current_count == max_count && current_number != frequent_number)
        {
            if (current_number < frequent_number)
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

    scanf("%d", &n);
    int *data = new int[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data[i]);
    }

    int answer = getFrequentNumber(data, n);

    printf("%0.4d", answer);

    delete[] data;
    return 0;
}