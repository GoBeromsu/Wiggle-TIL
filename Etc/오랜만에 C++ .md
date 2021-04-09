## 친구 과제 도와주려고 오랜만에 만져보았다

```c++
#include<iostream>

int main(){

    double fahrenheit = 0;
    double celcius = 0;
    
    std::cout << "섭씨 온도를 입력하시오 ";
    std::cin >> celcius;
    
	 fahrenheit = celcius * 9/5+ 32;
	
    std::cout << " 화씨 온도는 " << fahrenheit;
    return 0;

}
```

간단한 문제야서 코드가 길진 않았다

###놓쳤던 것들 && 까먹은 것들

* 코드를 순차적으로 컴파일러가 읽는걸 간과했다
	* 왜 값이 32만 나오나 했는데 온도 변환식을 위에 선언했다
	* 내가 원하는 대로 하려면 함수를 따로 선언해 불렀으면 됬을거다
* C++에서 >>, <<의 뜻이 헷갈렷다
	* 리눅스랑 연관지어 기억했었는데 가물가물하다
