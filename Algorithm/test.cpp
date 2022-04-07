#include <stdio.h>
#include<iostream>
#include <vector>
#include <time.h>
#include <algorithm>

#pragma warning(disable:4996)
using namespace std;

vector<vector<int>> Perms;
vector<int> sums;
vector<int> testTime;

void repeatPermutation(vector<int> vec, vector<int> perm, int depth)
{   
    int sum = 0;

    if (depth == perm.size())
    {
        for (int i = 0; i < perm.size(); i++)
        {
            sum += perm[i];
        }

        if (sum == perm.size()) {
            for (int i = 0; i < perm.size(); i++)
            {
                cout << perm[i] << " ";
            }
            cout << endl;
          /*  Perms.push_back(perm);
            sums.push_back(sum);*/
        }
        return;
    }

    for (int i = 0; i < vec.size(); i++)
    {
        perm[depth] = vec[i];
        repeatPermutation(vec, perm, depth + 1);
    }
}


int process(int N, int m, vector<int> testTime) {
    int time = 0;

    vector<int> numbers(N-m+1,0);
    vector<int> perm(m);
  
    for (int i = 1; i < N - m + 1; i++) {
        numbers[i]=i; 
    }
    repeatPermutation(numbers,perm , 0);  // {'a', 'b'}의 길이 3의 중복순열 모두 출력하기

    //int max = 0;
    //int maxIdx = 0;

    //for (int i = 0; i < sums.size(); i++) {
    //    if (max < sums[i]) {
    //        max = sums[i];
    //        maxIdx = i;
    //    }
    //}
    //int mVal = 0;
    //int mIdx = 0;
    //for (int i = 0; i < Perms.size(); i++) {
    //    if (Perms[maxIdx][i] > mVal) {
    //        mVal = Perms[maxIdx][i];
    //        mIdx = i;
    //    }
    //}

    //time = mVal * (testTime[mIdx]);

    return time;
}



int main()
{
     // start와 finish 변수에 함수 실행 시간과 종료 시간 후 차를 duration에 저장합니다.
    // duration : 프로그램 실행 시간
    clock_t start, finish;
    double duration;


    int N = 0; int m = 0;

  
    scanf("%d\n", &N);
    scanf("%d\n", &m);

    testTime.clear();
    testTime.resize(m, 0);

    for (int i = 0; i < m; i++)
    {   
        scanf("%d", &testTime[i]);
    }
    start = clock();

    printf("%d\n", process(N, m, testTime));
    finish = clock();
    // 출력
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    cout << "실행시간:" << duration << "초" << endl;
    return 0;
}

