## 정보 수집

- 모의 해킹의 대상을 정하고 나면 가장 처음 수행하는 단계
- 수집할 정보
  - 웹 애플리케이션을 서비스하기 위한 호스트 환경 정보
    - 관련 취약점을 찾아 쉽게 공격 가능
  - 웹 애플리케이션 자체에 대한 정보
    - 웹 애플리케이션 매핑을 통해 애플리케이션 자체의 정보를 수집함으로써 그 구조를 파악하고 공격 지점을 찾을 수 있다.

### 배너를 통한 정보 수집(Simple)

- 배너 그래빙
  - 서버의 응답을 통해 정보를 수집하는 방법을 일컬음
  - 응답 메시지의 서버 헤더 확인하면 쉽게 웹 서버 정보를 얻을 수 있다.
- 응답 메세지(헤더)의 종류
  - 서버 헤더
    - 아파치 웹 서버 버전 정보, 운영체제, php 버전 정보, OpenSSL 정보 등
  - X-Powered-By
  - X-ASPNET-VERSION
- 응답 헤더 정보 확인하는 방법
  - 브라우저의 개발자 도구의 네트워크 탭으로 확인 가능하다
  - 버프 스위트의 프록시 히스토리 기능을 통해서도 확인 가능

#### 기본 설치 파일을 통한 시스템 정보 수집

- 웹 애플리케이션 운영을 위한 요소를 구성할 때 __기본 설치 파일__ 로 호스트 환경 정보가 노출 될 수 있다.

#### 웹 취약점 스캐닝

- 자동화된 프로그램을 이용하여 웹 사이트의 여러 가지 정보를 수집 및 취약점을 분석하는 방법
- 자동화 프로그램 예시
  - nikto -웹 스캐닝 툴

#### 디렉터리 인덱싱

- 웹 서버의 잘못된 설정으로 웹 서버 디렉터리의 파일들이 노출되는 취약점
  - 디렉터리 리스팅 취약점이라고도 불림
- 웹 서버의 기본 지원 기능을 이용한 취약점이다.
  - 중요한 파일 목록이 출력될 수도 있음
  - 소스코드나 개인정보가 노출 될 수 있어 치명적인 취약점이다.

#### 웹 애플리케이션 매핑

- 웹 애플리케이션의 메뉴와 링크를 따라가면서 어떤 url과 파라미터들이 전송되는지, 웹 애플리케이션 구조를 파악하는 과정
- 웹 애플리케이션의 기능과 동작을 쉽게 파악할 수 있음
  - 이는 공격 지점 선정하는데 도움이 됨

#### 수동 매핑

- 직접 웹 애플리케이션에 접속하여 각 메뉴를 확인하는 과정
  - 버프 스위트의 사이트 맵 기능을 활용할 수 있다.

#### 크롤링

- 크롤링을 이용하면 웹 애플리케이션 매핑 과정을 자동으로 수행할 수 있다.
  - 크롤링은 웹 페이지의 링크를 분석하여 새로운 웹 페이지를 찾아내는 과정
- 동작과정
  1. 크롤러가 처음 지정된 URL로 요청한다
  2. 처음 요청에 의해 전송 받은 응답 메시지를 분석하고, 응답에 포함된 링크를 각각 추가 요청한다.
  3. 링크 요청에 의해 전송 받은 응답 메시지를 다시 분석하고, 링크가 다시 포함되었으면 또 다시 링크를 추가 요청한다.
  4. 더 이상 링크를 찾을 수 없거나 에러 메시지가 응답될 때까지 이 과정을 반복하다

#### DirBuster

- URL 목록 파일을 사용하여 각 URL을 자동으로 입력해보는 방식으로 웹 애플리케이션의 구조를 파악한다.
- 숨겨진 페이지를 찾을 수 있음
- 브루트 포스 공격 : 목록 파일을 사용하여 정보를 찾는 기법

#### robots.txt

- 웹사이트의 정보를 수집하는 웹 로봇을 위한 설정 파일 -> 크롤러의 일종
- 웹사이트의 최상위 디렉터리에 위치시켜, 웹사이트의 정보 수집을 허용하거나 불허하는 명령을 내릴 수 있음
- 웹 사이트 운영자는 User-agent 키워드로 키워드 수집을 허용/차단 할 수 있다.
- 하지만 robots.txt를 따르는 것은 웹 로봇이다.
  - 악의적으로 disallow 키워드르로 차단된 정보를 수집하게 할 수도 있다.

### 정보 수집 대응 방법

#### 불필요한 정보 노출 삭제

- 서버 헤더에 제공 되는 정보를 삭제하여 전송하라
- 웹 서버 및 프레임 워크로 자체적으로 헤더를 삭제
- 웹 방화벽과 같은 보안 장비로 일괄 헤더 삭제

- 불필요한 기본 설치 파일들;과 백업 파일, 테스트 파일은 모두 외부에 노출되지 않도록하라

#### 스캐너/크롤러 차단

- 자동화 프로그램을 완전 방어하는 것은 불가능하다
- 적절한 로깅뫄 모니터링을 통해 어느 정도 공격 시도 탐지 및 차단 가능
- 탐지 방법
  - 웹 서버 접근 로그에 기록된 요청 헤더 정보와 접속 횟수를 확인
  - IDS/IPS나 웹 방화벽 등의 보안 장비를 사용해서도 자동화 공격 탐지 및 차단 가능

#### 디렉터리 인덱싱 설정 제거

- 웹 서버의 설정을 변경하여 대응이 가능하다
  - 아파치의 경우, 아파치 설정 파일의 Indexes 옵션을 제거