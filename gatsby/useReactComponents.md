## Use React Components

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

### About Page 작성
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

### <Link> 사용하는 법

수동으로 url을 추가할 때 유용한 방식이다.
html의 <a> 태그가 비슷하다.
```js
<Link to="/AboutPage/">About</Link>
```