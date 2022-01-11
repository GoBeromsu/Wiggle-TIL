## 문제

Given three integers (X,Y , and Z) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.

- If all three sides are equal, output EQUILATERAL.
- Otherwise, if any two sides are equal, output ISOSCELES.
- Otherwise, output SCALENE.

주어진 세 정수 X,Y,Z는 삼각형의 세 변의 길을 나타낸다. 삼각형의 상태가 무엇인지 알아내라

- 세 변의 길이가 같다면 EQUILATERAL
- 두 변의 길이가 같다면 ISOSCELES
- 나머지는 SCALENE

## 풀이

```sh
read x
read y
read z

if [ $x -eq $y -a $x -eq $z ]
then
    echo EQUILATERAL
elif [ $x -eq $y -o $y -eq $z ]
then
    echo ISOSCELES
else
    echo SCALENE
fi
```
