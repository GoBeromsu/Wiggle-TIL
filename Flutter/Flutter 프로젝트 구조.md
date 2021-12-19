# Flutter 프로젝트 구조 

기본적으로 flutter 앱은 runApp() 함수를 호출하며 시작한다.

```dart
void main() => runApp(Widget app);
```

runApp() 함수는 Widget을 인자로 받는다. runApp의 인자가 되는 Widget은 Widget tree의 root widget이 된다.

flutter에서는 각 위젯들이 부모-자식 관계를 가진다. 이러한 위젯들의 모인 구조를 widget tree라 하는데, flutter의 직관성은 여기서 온다.

## Reference

[Flutter Widget 소개](https://www.ride-or-die.info/flutter-widget-%EC%86%8C%EA%B0%9C/)

