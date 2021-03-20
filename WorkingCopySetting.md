# edtiorial - workingcopy Setting

마크다운 에디터로 editorial를 사용하기로 했다. 기능도 많은편이고 내 맘대로 working flow를 만들 수 있어 선택했다. 

icloud랑 동기화를 해서 사용할까 했는데 앱과 앱 사이에 중간 단계가 늘어나는 것 같아  editorial이랑 workingcopy document를 참고해서 workingflow를 만들었다

* [editorial docs](http://www.editorial-workflows.com)
* [workingcopy docs](https://workingcopyapp.com/url-schemes.html#writing)

x-callback url을 이용하니 간단했다. 자동화를 위해 만들어진 ios용 url이란다. app 사이의 연결성을 확대시켜준다. 개발자 입장에서 url을 통해 간단히 데이터를 주고 받을 수 있단게 큰 장점이라 생각한다

```shell
targetapp://x-callback-url/updateStatus?
   x-source=SourceApp&
   text=[User inputted string]
```

## 
