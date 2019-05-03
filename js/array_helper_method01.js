// var colors = ['red', 'blue', 'green',]

// for (var i =0; i< colors.length; i++){
//     console.log(colors[i])
// }

// const COLORS = ['red','blue','green']
// COLORS.forEach(function(color){
//     console.log(color)
// })
// COLORS.forEach(color => console.log(color))

// // 아래함수에 for을 forEach로 바꾸시오
// function handlePosts(){
//     const posts = [
//         {id:23, title:'daily news'},
//         {id:52, title:'Code City'},
//         {id:105, title:'The Ruby'},
//     ]
//     for (let i = 0; i< posts.length; i++){
//         savePosts(post)
//     }
// }

// function handlePosts(){
//     const posts = [
//         {id:23, title:'daily news'},
//         {id:52, title:'Code City'},
//         {id:105, title:'The Ruby'},
//     ]
//     posts.forEach(function(post){

//     })
//     posts.forEach(post => console.log(post))

// }
// // 아래코드의 images 배열안에 있는 정보를 곱해 넓이를 구하여 areas 배열에 저장하는 코드를 foreach 헬퍼를 사용해서 작성해보자
// const images = [
//     { height:10, width:30},
//     { height:20, width:90},
//     { height:54, width:32},

// ]
// const areas = []
// images.forEach(image => areas.push(image['height']*image['width']))
// console.log(areas)

// 2. map함수는 새로운 배열을 return한다.
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때
// map filter 는 모두 사본을 return 하며 원본 배열은 바뀌지 않는다.

const NUMBERS = [1,2,3,]

// const DOUBLE_NUMBERS = NUMBERS.map(function (number){

//     return number*2
// })

// console.log(DOUBLE_NUMBERS)
const DOUBLE_NUMBERS = NUMBERS.map(number => number*2)


// map 헬퍼를 사용하여, images 배열안의 object 들의 height 들만 저장되어 있는 heights를 반환
const images = [
    {height:'34px', width:'39px'},
    {height:'54px', width:'19px'},
    {height:'83px', width:'75px'},
]
const heights = images.map(image=>image.height)
console.log(heights)

// 2번
const trips = [
    {distance:34, time:10},
    {distance:90, time:50},
    {distance:59, time:25},

]
const speeds = trips.map(trip=>trip.distance / trip.time)
console.log(speeds)

// 3번
const brands = ['Marvel', 'DC',]
const movies = ['IronMan', 'BatMan',]

const comics = brands.map((x,i)=> ({name:x, hero: movies[i]}))
console.log(comics)

// filter 함수는 필터링 된 요소들만 배열로 return 한다.
const PRODUCTS = [
    { name: 'cucumber', type: 'vegetable' },
    { name: 'banana', type: 'fruit' },
    { name: 'carrot', type: 'vegetable' },
    { name: 'apple', type: 'fruit' },
 ]

const fruitProducts = PRODUCTS.filter(function(product){
    return product.type === 'fruit'

})
console.log(fruitProducts)

// exercise
const numbers = [ 15, 25, 35, 45, 55, 65, 75, 85, 95 ]

const filteredNumbers = 
console.log(filteredNumbers)
// 3-2 users 배열에서 admin 이 true 인 user object 들만 filteredUsers 배열에 저장하라.
const users = [
    {id: 1, admin: true},
    {id: 2, admin: false},
    {id: 3, admin: false},
    {id: 4, admin: false},
    {id: 5, admin: true},
]

const filteredUsers = users.filter(function(user){
    return user.admin === true
})