// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000)   // non-block, call back 스택에서 따로 실행되고 있음, 그러나 사용자가 보기에는 동시에 실행되는것 처럼 보임
// console.log('end')

// // 어떻게 파이썬처럼 할까?

// const logEnd = () => {
//     console.log('end program')
// }
// console.log('sleep')
// setTimeout(logEnd, 3000)

// function first(){
//     console.log('first')
// }

// function second(){
//     console.log('second')
// }

// function first(){
//     console.log('Third')
// }


// first()
// setTimeout(second, 0)  // 0초라고 하더라도, 콜백스택에 들어가야하기 때문에 딜레이 발생
// third()



function func1(){
    console.log('func1')
    setTimeout(func2,0)
    func3()
}

function func2(){
    console.log('func2')
}

function func3(){
    console.log('func3')
}

func1()




