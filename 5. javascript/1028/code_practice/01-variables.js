/*
  [let 키워드 연습]
  
  1. let 키워드를 이용하여 ssafy 변수를 작성하세요.
  2. ssafy 변수에 '제주도'를 할당하세요.
  3. ssafy 변수의 값을 현재 여러분의 지역으로 재할당하세요.
*/
// let 키워드는 재할당이 가능하다!!
let ssafy
ssafy = '제주도'
ssafy = '2동탄'

/*
  [const 키워드 연습]
  
  1. const 키워드를 이용하여 phone 변수를 작성하세요.
  2. phone 변수에 'Galaxy S2'을 할당하세요.
  3. phone 변수의 값을 현재 여러분의 핸드폰 기종을 재할당하세요.
  4. 재할당 에러를 확인하세요.
*/
// const 키워드는 재할당이 불가능하다!!
const phone
phone = 'Galaxy S2'
phone = 'iPhone 11 Pro'
// Uncaught TypeError: Assignment to constant variable.
// at <anonymous>:1:7

/*
  [블록 스코프 - let 예시]
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  console.log('블록 스코프:', fullName)
}

console.log('전역 스코프:', fullName)


/*
  [블록 스코프 - const 예시]
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  const language = 'Python'
}

console.log(language)
// Uncaught ReferenceError: language is not defined
    // at <anonymous>:1:13
// const 키워드로 선언된 language는 블록 바깥에서는 읽을 수 없다.


/*
  [var 키워드 연습]
  
  1. var 키워드를 이용하여 framework 변수를 작성하세요.
  2. framework 변수에 'Bootstrap'를 할당하세요.
  3. framework 변수에 'Django'를 재할당하세요.
  4. framework 변수를 재선언하고 'Vue'를 할당하세요.
*/
var framework = 'Bootstrap'
framework = 'Django'
var framework = 'Vue'
// Django가 출력 -> 개발자 도구의 설정때문
// -> console.log(framework) 해주면 Vue가 출력됨을 알 수 있다.


/*
  [함수 스코프 - var 키워드 예시]
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

function f1() {
  var message = 'You are doing great!'
}
console.log(message)
// Uncaught ReferenceError: message is not defined
    // at <anonymous>:1:13


/*
  [블록 스코프 - var 키워드 예시]

  Tip.
    if문은 블록 스코프를 생성합니다.
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

const codeEditor = 'vscode'

if (codeEditor === 'vscode') {
  var theme = 'dark+'
}
console.log(theme)


/*
  [블록 스코프 - const, let 키워드 예시]
  
  Tip. 
    const와 let은 블록 스코프입니다.
    함수의 중괄호도 블록에 해당됩니다.
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

function f2() {
  const stack = 'Last In, First Out'
}
console.log(stack)
// Uncaught ReferenceError: stack is not defined
    // at <anonymous>:1:13

function f3() {
  let queue = 'First In, First Out'
}
console.log(queue)
// Uncaught ReferenceError: queue is not defined
    // at <anonymous>:1:13


/*
  [호이스팅(hoisting)]
  
  아래 코드 실행 후 결과를 확인해보세요.
  그리고 const와 let의 경우와 비교해보세요.
*/

console.log(hoisted)
var hoisted = 'can you see me?'
// undefined 출력

console.log(lunch)
const lunch = '초밥'
// Uncaught ReferenceError: lunch is not defined
    // at <anonymous>:1:13

console.log(dinner)
let dinner = '스테이크'
// Uncaught ReferenceError: dinner is not defined
    // at <anonymous>:1:13