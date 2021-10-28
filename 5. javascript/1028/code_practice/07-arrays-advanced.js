/*
 [배열 관련 주요 메서드 연습 심화 1]
 
 속력(distance/time)을 저장하는 배열 speeds를 만드세요.
*/

const trips = [
  { distance: 34, time: 10 },
  { distance: 90, time: 50 },
  { distance: 59, time: 25 },
]
const speeds = []
trips.forEach((value) => {
  speeds.push(value['distance'] / value['time'])
})

// 다른 방법
const speeds = trips.map((element) => {
  return element.distance / element.time
})

/*
 [배열 관련 주요 메서드 연습 심화 2]
 
 주어진 배열의 요소 중 특정 문자(query)가 포함되는 요소만 모아서 새로운 배열을 반환하세요.
*/

const languages = ['python', 'javascript', 'html', 'java']
const query = 'java'
const result = []
languages.forEach((value) => {
  if (value.includes(query)) {
    result.push(value)
  }
})

// 다른 방법
const result = languages.filter((element) => {
  return element.includes(query)
})


/*
 [배열 관련 주요 메서드 연습 심화 3]
 
 주어진 배열을 사용하여 다음과 같은 객체를 만드세요.
 {
   smith: 90,
   peter: 80,
   anna: 85,
 }
*/

const scores = [
  { name: 'smith', score: 90 },
  { name: 'peter', score: 80 },
  { name: 'anna', score: 85 },
]
const scoreMap = scores.reduce((acc, score) => {
  acc[score.name] = score.score
  return acc
}, {})


/*
 [배열 관련 주요 메서드 연습 심화 4]
 
 주어진 accounts 배열에서 balance가 24,000인 사람을 찾으세요.
*/

const accounts = [
	{ name: 'justin', balance: 1200 },
	{ name: 'harry', balance: 50000 },
	{ name: 'jason', balance: 24000 },
]
const result = accounts.find((value) => {
  return value.balance === 24000
})
console.log(result)


/*
 [배열 관련 주요 메서드 연습 심화 5]
 
 주어진 requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
*/

const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]
const result = requests.some((value) => {
  return value.status === 'pending'
})
console.log(result)


/*
 [배열 관련 주요 메서드 연습 심화 6]
 
 주어진 users 배열을 통해 모든 유저의 상태가 submmited인지 여부를 확인하세요.
*/
const users = [
  { username: 'a', submitted: true },
  { username: 'b', submitted: false },
  { username: 'c', submitted: true },
]
const hasSubmitted = users.every((user) => {
  return user.submitted // === true
})
console.log(hasSubmitted)