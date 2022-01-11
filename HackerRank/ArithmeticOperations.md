# ArithmeticOperations

## 문제

A mathematical expression containing +,-,\*,^, / and parenthesis will be provided. Read in the expression, then evaluate it. Display the result rounded to decimal places.

여러 수학 기호들이 포함된 식이 주어질 것이다. 이 식을 계산하라. (결과 값은 반올림된 값이다)

## 풀이

```sh
read val

val=${val// /}

function Cut(){
    echo "scale=$1;${2}" | bc
}

bRound=`Cut 4 $val`

if [ ${bRound: -1} -eq 5 ];then
    dest=`echo "${#bRound}-1" | bc`
    echo "${bRound:0:$dest}+0.001" | bc
else
    Cut 3 $val
fi
```
