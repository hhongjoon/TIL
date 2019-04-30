var _ = require('lodash')
let list = ['짜장면','짬뽕','볶음밥',]
let pick = _.sample(list)
let numbers = _.range(1,46)
let menu = {
    짜장면:'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg',
    짬뽕:'http://cfile227.uf.daum.net/image/15224F524DA1CE942FA7F4',
    볶음밥:'http://recipe1.ezmember.co.kr/cache/recipe/2015/07/30/9097c31c08072ba81bfb367e45c48dff1.jpg',
}
console.log(`오늘의 메뉴는 ${pick}입니다.`)
let lottery = _.sampleSize(numbers,6)
console.log(menu[pick])
console.log(`행운의 번호: ${lottery}`)

let getMin = (a, b) => {
    if (a>b){
        return b
    }
    return a
}

let getMinFromArray = nums => {
    let min = Infinity
    for (num of nums){
        if (min > num){
            min = num
        }
    }
    return min
}
ssafy = [1,2,3,4,5,]
console.log(getMinFromArray(ssafy))