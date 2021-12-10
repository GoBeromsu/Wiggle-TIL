# What is Widget

Flutter에서는 모든 것이 위젯이라 할 수 도 있습니다. 어떻게 보면 앱 그 자체도 하나의 위젯이라 생각됩니다

UI를 구성하는 모든 요소, 눈에 보이지 않는 요소들(Padding,Column ..)까지 위젯입니다

## Types of Widgets

Flutter에서의 위젯 타입은 Stateless,Stateful 등이 있다.

### Statelestt

움직임이나 변화가 없는 정적인 상태이다. 스크린 상에 존재할 뿐 아무것도 하지 않는다. 어떠한 실시간 데이터도 저장힞 않고, 어떤 변화를 유발시키는 value를 가지지 않는다.

### Stateful

계속 움직임이나 변화가 있는 상태이다. value 값을 지속적으로 추적 및 보존한다. 사용자의 interation에 따라 상태가 바뀐다.


## Widget tree

Widget들은 tree 구조로 정리될 수 있다. 한 Widget 내에 얼마든지 다른 Widget들이 포함 될 수 있다. 

Widget tree 구조는 부모 widget과 자식 widget으로 구성된다. 

parent widget을 widget containter라고 부르기도한다
