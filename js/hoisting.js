// let 블록 스코프 예제
// {
//     let x = '정운지'
//     console.log(x)
//     {
//         let x = 1
//         console.log(x)
//     }
//     console.log(x)

// }
// console.log(typeof x)

//var로 선언하면 현재 스코프 안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수 있따.

//let으로 선언하면 그 변수는 선언하기 전에는 존재하지 않는다.

// 선언되지 않으면 에러 / undefined변수이면 에러X
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
let foo

let bar = undefined

let x = 1

// 변수선언하지 않았는데 접근할 수 있는 현상 발생