# 버프 스위트

- HTTP 프록시
  - 사용자와 웹 서버 가운데 위치
  - 서로 간의 HTTP 요청과 응답을 중간에서 전달하는 역할
  - 웹 사용자의 시스템 내부나, 외부 인터넷 구간에 위치
  - 웹 브라우저를 통해 HTTP 요청을 전송 - 요청 메시지 인터셉트 - 메시지 내용 확인/수정 - 네트워크 전송
  - 기본 프록시 주소 : 127.0.0.1:8080(로컬 호스트 주소,루프 백 주소)
- 폭시 프록시 애드온
  - 파이어폭스 proxy 툴

### HTTPS 사이트 접속 문제

- 해당 사이트를 접속할 때 인증서를 신뢰하지 못해 발생하는 문제
- Burpsuit가 중간에서 자기의 인증서를 서버 인증서 대신 웹 브라우저에 보냄
  - 버프 스위트/웹 브라우저/ 버프 스위트/웹 서버가 SSL 연결을 해야한다.
    - 웹서버 인승서 대신 버프 스위트의 인증서를 보게 됩니다.

### 버프 스위트의 기능

#### Target

- 사이트 맵
  - 접속한 모든 호스트와 URL 구조 파악 가능
  - 트리 구조 및 호스트 간 보낸 요청과 응답 정보를 간략하게 보여줌
    - 응답 정보 : 메소드와 URL, 파라미터 존재 여부, 응답 코드, 응답 메시지의 길이)
  - Filter 기능 지원
- scope
  - 버프 스위트는 기본적으로, 자신을 거친 모든 정보를 표시
  - 얻을 정보를 제한 가능

### 프록시(Proxy)

#### 인터셉트

- 웹 브라우저와 웹 서버가 주고 받는 http 요청/응답 메시지 내용을 변경할 수 있음
  - 사용자가 메시지를 전송할 때가지는 전달 되지 않음
- HTTP는 자체적으로 타임 아웃을 처리하지 않음
  - 인터셉트를 장시간 했다가 메시지를 전송해도 통신에 지장 없다
  - 세션 타임아웃이 적용된 웹사이트의 경우 예외
  - HTTP 요청의 모든 부분을 공격자가 조작하는 것이 가능

#### HTTP History

- 접속 기록을 시간 순으로 정렬하여 보여준다

#### 옵션

- 프록시와 관련된 옵션 설정
  - Proxy listeners
  - Intercept client Requests
  - Intercept Server Responses
  - Response Modification
  - Match and Replace

### Spider

- 웹 사이트의 링크를 자동으로 찾아, 웹 사이트 전체 구조를 알아냄 - 크롤링
- 사이트 구조를 따라가다 검증이 필요시, 입력만 하면 추가적인 정보 얻을 수 있음

### 인트루더

- 요청 메시지의 특정 위치를 지정하여 여러 개의 데이터를 자동으로 반복해서 전송하는 기능
  - 페이로드 : 이 때 보내는 데이터
- 타깃(공격 대상 설정) : 호스트 주소와 포트 지정
- 포지션 : 공격 종류를 선택
  - 페이로드 입력 위치 등 수정
- 페이로드
  - 어떤 페이로드를 입력하여 테스트할지 결정

### 리피터

- 수동으로 메시지를 조작하며 반복적인 테스트를 하기 위한 기능

### 스캐너(유료)

- 웹 애플리케이션의 보안 취약점을 자동으로 찾는 기능

### 시퀀서

- 세션 값 추측 또는 세션 값이 얼마나 랜덤하게 생성되는지 테스트
  - 성공하면 세션 하이재킹 공격 가능성 상승

### 디코더

- 각종 문자열의 인코딩, 디코딩 값을 확인하는데 사용
  - 인코딩 된 값을 쉽게 디코딩 할 수 있음

### 컴페어러

- 두 개의 요청 메시지나 응답 메시지를 일대일로 비교하여 두 메시지 간의 차이점을 알아냄

### 익스텐더

- 자신이 개발한 코드나 서드 파티에서 개발한 확장 기능을 추가로 설치하여 사용 가능