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

## 내 설명이 어려웠다

다시 친구에게 연락이 왔다. 어떻게 해야하는지 모르겠다고 했다. 내가 어떻게 잘못 알려줬을까

* 컴퓨터가 코드를 읽는 순서를 가르쳐주지 않았다
	* 순차적으로 위에서 아래, 왼쪽에서 오른쪽으로 읽는 것을 말안했다
* 변수의 초기화 개념을 말하지 않았다

```c++
#include<iostream>

int main(){

// 변수의 이름을 바꾼다
// = 0;은 변수를 초기화 하는거야

    double radius= 0;
    double length = 0;
    double volume = 0;
	
	//std::cout << ""는 따옴표 안의 글들을 출력하란 소리
    std::cout << "반지름과 높이를 입력하시고 ";
	// std::cin >> (변수 이름)은 변수를 입력받는다는 소리
    std::cin >> radius;
    std::cin >> length;
	
	//아래는 식을 적는거야
	//컴퓨터가 코드를 차례대로 읽어 내려오니까 식은 변수보다 아래에 적어야해
	volume = radius * radius * length * 3.14;
	
	// std::cout할 때 << volume이런 식으로 변수의 값을 출력할 수 있어
	
    std::cout << " 용적은 " << volume;
    return 0;

}
```

* 위와 같이 다시 주석을 달고 카톡으로 처음 보냈던 코드와 비교하면 이해가 될거라고 말해주었다
* 무조건 답을 알려주는건 서로에게 좋지 않을 것 같다

## 랜덤 함수 값 구하는 문제

```c++
#include <iostream>
#include <ctime> // for time function
#include <cstdlib> // for rand and srand functions
using namespace std;

int main()
{
   // 1. Generate two random single-digit integers
   srand(time(0));
   int number1 = rand() % 10;
   int number2 = rand() % 10;
   int number3 = rand() % 10;

   cout << "What is " << number1 << " + " << number2 << " + " << number3 << "? ";
   int answer = 0;
   
   answer = number1 + number2 + number3;
   // 4. Grade the answer and display the result
   if (answer > 100){
   	cout << "합이 100을 초과했습니다";
   }
   else{
   	cout << "합은 " << answer;
   }
   
   
   return 0;
}
```

친구가 어려웠던 부분은 원래 위의 코드 짜는데 참고하라고 랜덤한 두 수의 차를 구하는 코드를 교수님이 주셨는데 오히려 그게 더 과제할 때 헷갈리게 했나보다

### 이스케이프 문이 안먹힌다?

```c++
#include <iostream>

using namespace std;

int main()
{
  int number=0;
  
  cout << "Enter an integer ";
  cin >> number;
  cout << "\n";
  
  cout << "Is " << number  << " divisible by 5 and 6? ";
  if(number%5==0 && number%6==0){
  	cout << "true \n";
  }else{
  	cout << "false \n";
  }
    
  cout << "Is " << number  << " divisible by 5 or 6? ";
  
  if(number%5 ==0 || number%6==0){
  	cout << "true \n";
  }else{
  	cout << "false \n";
  }
  
  cout << "Is " << number  << " divisible by 5 or 6?, but not both ";
  

    if((number%5 ==0 &&number%6!=0)|| (number%5 !=0 && number%6==0)){
  	cout << "true \n";
  }else{
  	cout << "false \n";
  }
  
  return 0;
}

```

* 이스케이프 문을 입력했는데 안먹혀서 먼가했다
	* 핸드폰에 ₩n이랑 \n 둘다 있어서 그냥 썼는데 줄이 안바뀌었다
	* \n으로 하니까 바뀌더라
* 그거말곤 어려움 없는 문제였다
