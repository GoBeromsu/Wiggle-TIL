#include <stdio.h>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_LENGTH = 100000;

class MyString
{
private:
    char *characters;
    int length;

public:
    MyString(const char *str)
    {
        this->length = strnlen(str, MAX_LENGTH);
        this->characters = new char[this->length];
        for (int i = 0; i < this->length; i += 1)
        {
            this->characters[i] = str[i];
        }
    }
    MyString(const string &original)
    {
        this->length = original.length();
        this->characters = new char[this->length];
        for (int i = 0; i < this->length; i += 1)
        {
            this->characters[i] = original[i];
        }
    }
    bool operator<(const MyString &o) const
    {
        int n = min(this->length, o.length);
        // 문자열을 하나씩 비교하며 글자가 다른 경우 누가 사전 순으로 앞서는지 확인한다
        for (int i = 0; i < n; i++)
        {
            // this가 o 보다 사전 순으로 앞선다면 true 아니면 false를 출력한다.
            if (this->characters[i] < o.characters[i])
            {
                return true;
            }
            else if (this->characters[i] > o.characters[i])
            {
                return false;
            }
        }
        // 위의 반복문에서 탐색을 마치면 글자는 모두 같지만 길이가 다른 경우만 남는다.
        // 두 문자열의 길이를 비교하여  this가 더 길면 true, 아니면 false를 출력한다
        if (this->length < o.length)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    bool operator>(const MyString &o) const
    {
        int n = min(this->length, o.length);
        // 문자열을 하나씩 비교하며 글자가 다른 경우 누가 사전 순으로 앞서는지 확인한다
        for (int i = 0; i < n; i++)
        {
            // this가 o 보다 사전 순으로 앞선다면 true 아니면 false를 출력한다.
            if (this->characters[i] > o.characters[i])
            {
                return true;
            }
            else if (this->characters[i] < o.characters[i])
            {
                return false;
            }
        }
        // 위의 반복문에서 탐색을 마치면 글자는 모두 같지만 길이가 다른 경우만 남는다.
        // 두 문자열의 길이를 비교하여  this가 더 길면 true, 아니면 false를 출력한다
        if (this->length > o.length)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    bool operator==(const MyString &o) const
    {
        int n = min(this->length, o.length);
        // 두 문자열의 길이가 다를 경우 서로 다른 문자열임이 자명하기에 바로 false를 리턴한다.
        if (this->length != o.length)
            return false;
        for (int i = 0; i < this->length; i++)
        {
            // 순차적으로 같은 인덱스의 글자를 비교해 나가며 다를 경우, 탐색을 중단하고 false를 리턴한다.
            if (this->characters[i] != o.characters[i])
            {
                return false;
            }
        }
        // 모든 탐색을 마쳤다면 두 문자열이 같은 경우이므로 true를 리턴한다
        return true;
    }

    ~MyString()
    {
        delete[] characters;
    }
};

int main()
{
    string s1;
    string s2;
    cin >> s1 >> s2;

    MyString mys1(s1);
    MyString mys2(s2);

    if (mys1 < mys2)
    {
        printf("-1");
    }
    else if (mys1 > mys2)
    {
        printf("1");
    }
    else
    {
        printf("0");
    }

    return 0;
}
