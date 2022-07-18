# Gettingstartedwithconditionals

## 문제

Read in one character from STDIN.
If the character is 'Y' or 'y' display "YES".
If the character is 'N' or 'n' display "NO".
No other character will be provided as input.

입력 값으로 한 문자를 받아라

만약 주어진 문자가 Y 또는 y 라면 YES,
주어진 문자가 N 또는 n 일 경우 NO를 출력하라

다른 입력 값은 주어지지 않는다

## 풀이

```sh
read val

Lowercase()
{
 echo $* | tr "[A-Z]" "[a-z]"
}


if [ $(Lowercase $val) == "y" ]
then
    echo "YES"
else
    echo "NO"
fi
```
