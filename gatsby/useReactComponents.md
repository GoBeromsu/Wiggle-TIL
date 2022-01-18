# Use React Components

리액트로 페이지를 만든다면 이 페이지는 여러 요소들로 이루어져있다.
이 때 큰 구성 요소들은 작은 구성 요소들로 이루어져있다.

내부적으로 리액트 구성요소는 리액트 요소를 반환하는 함수 있다.

* React Components == 리액트가 Dom Component를 렌더링하는데 사용하는 객체

```js
const hello = <h1>Hello world!</h1>

const Greeting = () => {
  return (
    <h1>Hello world!</h1>
  )
}
```

## About Page 작성
```javascript
import * as React from "react"

const AboutPage = () => {
    return (
        <main>
            <title>About Me</title>
            <h1>이렇게 하는 건가?</h1>
        </main>
    )
}

export default AboutPage
```

난 about page를 scr/pages 내에 생성할 것이다.
개츠비에서는 별도 api를 사용하지 않는 한 src/page 디렉터리에 생성된 페이지는 파일 이름을 페이지 경로로 한다.

## <Link> 사용하는 법

수동으로 url을 추가할 때 유용한 방식이다.
html의 <a> 태그가 비슷하다.
```js
<Link to="/AboutPage/">About</Link>
```

## 재사용 가능한 레이아웃 구성 요소 만들기

리액트에서는 반복되는 페이지들을 하나 하나 변경하는 것보다 모든 공통 요소들을 그룹화해서 하나의 요소로 만들어 사용한다.


React에는 __children__ 이란 개념이 있다.

구성 요소를 렌더링할 때 children은 해당 구성 요소의 prop을 자동으로 전달한다.

일종의 래퍼라 생각하면 된다.
```js
import React from 'react'
import Frame from '../components/frame'

const GalleryPage = () => {
  return (
    <Frame>
      <p>This will be passed in as children</p>
    </Frame>
  )
}

export default GalleryPage
```
```js
import React from 'react'

const Frame = ({ children }) => {
  return (
    <div>
      <h1>This is the page title</h1>
      { children }
    </div>
  )
}

export default Frame
```

위의 코드를 보면 내가 정의한 모듈 Frame을 태그로 불러와서 사용한다.
그러면 Frame의 구성 요소들을 출력한 후 Frame 태그 안의 값들을 출력한다.

이걸 좀 더 응용하면 props 값을 더 구체적으로 정의하여, 필요한 곳에 children을 사용하여 원하는 곳에 요소들을 자동으로 출력하고, 변화를 줄 수 있다.