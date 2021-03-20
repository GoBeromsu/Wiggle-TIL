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

## workingcopy dir을 editorial로 Copy

포스트 내용을 수정할 때마다 복붙하는게 불편해서 해결 방안을 찾아보았다

[shortcut](https://github.com/somelinguist/EditorialWorkingCopySync)을 이용해 repo 변경 사항을 에디터로 업데이트 하게했다.

shortcut 한 번 누르고 에디터 들어가서 바로 수정하니까 편하다 주의사항은 덮어쓰기 되는거라 잘못하면 적은거 다 날라간다

## editorial에서 Working Copy로!

x-callback url을 이용하면 커밋까지 한 번에 workflow를 할 수도 있고 이래저래 어떻게 써먹을까 고민 중이다

