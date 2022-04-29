#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <time.h>
using namespace std;

const int startTime = 540; // 09:00 즉 처음 버스가 운행하는 시간을 저장한 상수입니다.
const int askii = 48;      // 문자열을 정수로 변환할 때 아스키 코드와 0~9를 매칭할 때 사용할 상수입니다.

vector<string> split(string input, char delimiter)
{ //공백을 기준으로 슬라이싱하여 string 벡터에 차례대로 넣어주는 함수

    vector<string> result;  //슬라이싱된 string들을 저장할 string 벡터 선언
    stringstream ss(input); // stringstream 객체 ss를 선언하고  input 문자열 (공백이 포함되어있는 문자열)로 초기화
    string temp;

    while (getline(ss, temp, delimiter))
    { //입력스트림 객체인 ss에서 delimiter를 만날때까지의 string을 뽑아내temp에 저장
        result.push_back(temp);
    }
    return result;
}

int main()
{

    // n, t, m 값을 입력 받는다.
    int n, t, m;
    scanf_s("%d %d %d", &n, &t, &m);

    vector<string> timetables; // 학생들의 도착시간을 각각 문자열로 저장하는데 사용할 string 벡터입니다.
    string timetable;          // 처음 입력 받은 학생들의 시간 문자열을 저장할 변수입니다.
    vector<int> times;         // 학생들의 정류소 도착시간을 정수로 저장할 벡터입니다.
    int time = 0;              // string -> int로의 변환에서 시간을 정수로 임시 보관할 변수입니다.

    // pair 벡터에 first는 현재 회차 버스에 탄 사람의 수를 저장하고, 해당 버스에 탄 사람 중 마지막에 정류장에 도착한 사람의 시간을 저장합니다.
    // 결국은 전남이는 제일 마지막 버스의 마지막 사람으로 탄다면 최대한 늦잠을 잘 수 있다.
    vector<pair<int, int>> bus;
    bus.resize(n);                      //버스는 n회 운행을 하므로 bus 벡타의 크기를 n으로 resize한다.
    int personIndex = 0, bustIndex = 0; //사람과 버스가 몇 번째 왔는지 저장할 변수 입니다.
    //학생들이 정류장에 도착한 시간을 입력 받는다.
    cin.ignore();                       //버퍼에 앤터가 남아있으면 getline에서 이미 입력을 받은 것으로 처리하기 때문에 getline전에 버퍼를 비워줍니다
    getline(cin, timetable);            //엔터가 들어오기 전까지 공백을 포함하여 문자열 입력받습니다.
    timetables = split(timetable, ' '); // split 함수를 이용해서 입력받는 문자열을 공백을 기준으로 슬라이싱 (c++은 spilt 함수를 지원하지 않기때문에 직접 구현)

    // 실행 시간 계산에 쓰일 변수를 선언한다.
    clock_t start, finish;
    double duration;
    start = clock();
    // 계산의 편의를 위해 입력 받는 시간들을 전부 분으로 변환합니다.
    for (int i = 0; i < timetables.size(); i++)
    {
        string currentTime = timetables[i];                                                                                                                  //현재 시간을 저장하는 임시 변수입니다.
        time = ((int(currentTime[0]) - askii) * 10 + (int(currentTime[1]) - askii)) * 60 + (int(currentTime[3]) - askii) * 10 + int(currentTime[4]) - askii; //문자열의 각 인덱스를 아스키 코드와 매핑하여 정수로 바꾼 후 분으로 치환합니다.
        times.push_back(time);                                                                                                                               // 계산된 시간을 정수 배열 times에 저장합니다.
    }
    // 입력 받은 시간들을 정렬합니다.
    // 순차적으로 학생들의 정류소 도착 시간과 버스 출발 시간을 비교하기 위함입니다.
    sort(times.begin(), times.end());

    // 학생들이 아직 버스를 다 타지 않았고, 오늘 배정된 셔틀버스가 모두 운행 하지 않은 동안만 탐색을합니다.
    while (personIndex < times.size() && bustIndex < n)
    {
        if (times[personIndex] <= 540 + t * bustIndex)
        { //학생이 도착한 시간이 정류장의 이번 회차 출발 시간보다 작다면 버스를 탈 수 있습니다.
            if (bus[bustIndex].first >= m)
            {
                bustIndex++;
            }                                                                       //셔틀 버스에 사람이 꽉 찼다면 다음 회차 버스로 이동한다.
            bus[bustIndex].second = max(bus[bustIndex].second, times[personIndex]); // 현재 버스를 탄 사람 중 가장 마지막에 정류장에 도착한 사람을 저장한다.
            bus[bustIndex].first++;                                                 //매 회 한 명씩 태우고 있으므로 버스 인원을 1명 추가한다.
            personIndex++;                                                          //사람도 1명 추가한다.
        }
        else
        {
            bustIndex++; //현재 도착한 학생이 버스 시간을 넘어 도착했으므로 다음 버스로 가기 위해 인덱스를 더 해줍니다.
        }
    }
    int jn = startTime; // 전남이의 도착 시간을 저장할 변수를 선언합니다, 전남이가 제일 늦게 탄 시간 중 가장 빠른 시간은 09:00 이므로 첫 버스 운행시간으로 초기화합니다.
    if (bus[n - 1].first < m)
    {                                 //마지막 버스에 여석이 있다면 전남이는 그냥 마지막 버스를 타면 된다.
        jn = startTime + t * (n - 1); // 전남이의 출발 시간은 마지막 버스의 운행 시간이 된다.
    }
    else
    {                               //마지막 버스에 여석이 없는 경우이다. 즉 마지막 버스의 마지막 사람보다 최소 1분 먼저 와야한다.
        jn = bus[n - 1].second - 1; // 그러므로 마지막 도착한 사람의 도착 시간에서 1을 빼준다.
    }

    string result; // 입력 받은 시간을 분으로 변환했으므로, 다시 계산 결과를 시간으로 바꿔 줘야한다.
    // 시간에서 몇 시인지 먼저 변환을 해서 result에 더한다.
    int hour = jn / 60;
    if (hour < 10)
        result = '0' + to_string(hour);
    else
        result = to_string(hour);

    result = result + ':';
    // "**:" 형태까지 만들어졌으므로, 나머지를 분으로 바꿔 result에 더하고 출력한다.
    int min = jn % 60;
    if (min < 10)
        result = result + '0' + to_string(min);
    else
        result = result + to_string(min);

    // 출력
    // 실행 시간과 결과 값을 출력합니다.
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    cout << result << endl;
    cout << "실행시간: " << duration << "초" << endl;
}