#include <stdio.h>
#include <iostream>

using namespace std;

int getMax(int x, int y)
{
    if (x > y)
    {
        return x;
    }
    else
    {
        return y;
    }
}

int main()
{
    int p, q;

    scanf("%d %d", &p, &q);
    int answer = getMax(p, q);
    
    printf("%d\n", answer);
    return 0;
}