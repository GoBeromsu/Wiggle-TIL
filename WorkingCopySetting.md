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

x-callback url을 이용하면 커밋까지 한 번에 workflow를 할 수도 있고 이래저래 만들었다

* 요구사항
	* overwrite 기능
	* til repo에 바로 저장
	* 파일 이름과 확장자 그대로 저장

위 요구사항을 반영해서[Til Workflow](editorial://add-workflow?workflow-data-b64=eNrVV91u2zYUfhVCwNINkJ2k7ZrNQGCkbrplCJoicZai82DQ0pHNmSI1krJiGAb2NHuwPck-UrKtJLtYbtLmxpHO__edo0NmFYlEq6gX5UL5J9uxOhFcdqbCzcrJmEvXLdQ0iiOeOAF91PttFRW8tPSWMm3oslRKwKCXcWkprlU3cNalu5rpCrqP3PCcHBm7tUpK63Q-FE4SciN6IrmFOrrRZp5JXZ2EbD-RO02F02ZIty7ywXeRVlGmZUqpV10U3jrqHcQt4SUVkieUk3II_M9ff0frdfx0tV-hbPqVG8EnMLxfu8IzXLiUUC24LMlL3bII0nTBVVKjgNrpOalLrqYUXFcHMTtcw-xMFaWL1jDwdr2oD4BfHUJDhX4sxB2kGyOmU0md4dn5E4PD6L0Xkj54FPehCZXIMqX3ftTMNnAjPb11pGwYR2dK-vo6kgGWqmE908EbaIWt4Cm-DzHROQTCajUMiF7GEd0WhqxvyMvHz1-pnC8m9WB3gQ4fT1kg_IsyZrWki9L5zt1nrS7qsdz4T4MJy3YcPVNI0erVnTbF0er1USMI62uHeTCjZM4WzRc2UiPllwRTDRUv-i9Gyru0JU-_lYuN5AEtFtF_vn63jYnnbcAv8wmfqvR-lU9ayEVB6vry_AFTGvIz7PDDOPLq_z1KR4fN5HxD4ebSa63b1ZvX7bGC4PvNnNUXgdXRq__w7tD2SNlNYgUUAN5JdLHsjfZH-7edBEEmPJl3SiNH-5URjkb7_Tktj88_f_o0_PGXdz983vPux_09XwD-FNzNjvvd_l6uUzrWCzLBzecxtCAu3xpdWTInJbjkTvgUy_pgQyV80rp4gaXeeIzf8enV4OTj6XgcyKu4cNfYEPJcc1zMmvY8ly_i93hzat7UfLMB-P52KOR3iJSSTYxoKNgmZQDEnOHKZmSM9_FNtCwzOmftMMxpVl9vceFmXKXMd4_xKReq63fLzYwU85RTyiqQwYQ_eGMmHF6lZIWAuZsR28xYnaOWGOuYFIpC4NDVoND4MUFhEQ4VuBnWlA8Qs2omkhmT5OzdOhNDHO6cKaqCaV0NjsOUMkRKGf5zwIi6Lhu2q_FSYLHwLJX4s8RGTGElMoESPEsGt_N8QoGkCnWRhzYhqdXUIpZmfKFFyjZzueNSqBZzkyXLhXV8DggeIupaCF3aTVWW6azx40gBCr1_g9AD7E74fMt34KPa9BLPrQZgGkHnsu5DyNVOEd5LY_Bes-QDoWwY1J0F221eQ48HM787GLdz3F1ywN8cLt76gImMLXXJ_sCks4ojMKSWL-quKu3Z8r6oD4o6QggL7kC8Q-lN20Ch3yB1nW2EKaHhmAvfjdC1oNbN4BRk0Kg8sH2X9Qfj3I3W_wK_dBzR)를 만들었다.

링크를 눌러 다운로드 받아서 사용하면 된다.

사용할 따 Key랑 repository 이름은 바꿔야한다. 내 꺼로 등록되어 있어서 그대로 실행하면 오류 뜰 것이다

### 삽질

* url escape variable을 체크 안해서 실행 오류가 발생했다
	* 커스텀 변수를 url에 추가할 땐 꼭 체크하자
