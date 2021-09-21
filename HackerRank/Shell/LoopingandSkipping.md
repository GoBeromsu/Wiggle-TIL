## 문제

Your task is to use for loops to display only odd natural numbers from  1 to 99 .

루프를 사용해서 1부터 99까지 출력하라
(각 요소들의 차가 2씩 나야한다)

## 풀이

```SH
for var in {1..99..2}
do
    echo $var
done
```