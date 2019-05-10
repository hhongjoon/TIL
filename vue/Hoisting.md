Hoisting

```
JS 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조 가능
끌어올려진 변수는 undefined
```



- var: 함수스코프 / 스코프안 사용가능, 선언전에도 사용 가능
- let: 선언하기 전 존재X

```
x	// undefined
var x = 1
x	// 1

var 변수는 선언전 언급 가능 / 함수나 전역스코프 전체를 살펴보고 var로 선언한 변수를 가장 위로 끌어올린다.
```



#### 콜백함수

-  setTimeout

비동기식 처리 모델이란 호출될 함수(콜백함수)를 미리 매개변수에 전달하고 처리가 종료하면 콜백함수를 호출하는 것이다.



#### Array Helper Method

COLORS.foreach(color => console.log(color))

images.foreach(function(image){

​	areas.push(image.height * image.width)

})

const DOUBLE_NUMBERS = NUMBERS.map(number => number *2)

const comics = brands.map((x,i) => ({name:x, hero: movies[i]}))

