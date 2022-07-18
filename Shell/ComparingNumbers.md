# ComparingNumbers

## 문제

Given two integers,  and , identify whether  or  or .

Exactly one of the following lines:
- X is less than Y
- X is greater than Y
- X is equal to Y


주어진 정수 X,Y의 크기를 서로 비교하라

결과에 따라 아래 문장 값을 출력하라
- X is less than Y
- X is greater than Y
- X is equal to Y


## 풀이

```sh
read valX
read valY

if [ $valX -eq $valY ]
then
    echo "X is equal to Y"
elif [ $valX -gt $valY ]
then
    echo "X is greater than Y"
elif [ $valX -lt $valY ]
then
    echo "X is less than Y"
fi
```
