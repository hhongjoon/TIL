
// var numbers = [1,2,3,4,5,]

// const numbersAddEach = numbers => {
//     let sum = 0
//     for(const number of numbers){
//         sum += number
//     }
//     return sum
// }
// numbersAddEach(numbers)
// console.log(numbersAddEach(numbers))

// // 배열로 이루어진 숫자들을 모두 빼는 함수
// const numbersSubEach = numbers =>{
//     let sum = 0
//     for(const number of numbers){
//         sum -= number
//     }
//     return sum
// }

// // 배열로 이루어진 숫자들을 모두 곱하는 함수
// const numbersMulEach = numbers =>{
//     let sum = 1
//     for(const number of numbers){
//         sum *= number
//     }
//     return sum
// }

// console.log(numbersAddEach(numbers))
// console.log(numbersSubEach(numbers))
// console.log(numbersMulEach(numbers))


// //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

// const numberEach = (numbers, callback) => {
//     let acc
//     for (const number of numbers){
//         acc = callback(number,acc)
//     }
//     return acc
// }

// const addEach = (number, acc = 0) => {
//     return acc + number
// }

// const subEach = (number, acc = 0) => {
//     return acc - number
// }

// const mulEach = (number, acc = 1) => {
//     return acc * number
// }

// console.log(numberEach(numbers, addEach))
// console.log(numberEach(numbers, subEach))
// console.log(numberEach(numbers, mulEach))

// numbersEach 이후의 제어들을  우리가 함수 정의 없이 매번 자유롭게 하려면?
const NUMBERS = [1,2,3,4,5,]
const numbersEach = (numbers, callback) => {
    let acc
    for (let i = 0; i< numbers.length; i++){
        number = numbers[i]
        acc = callback(number,acc)

    }
    return acc
}

console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc = 1) => acc * number))





