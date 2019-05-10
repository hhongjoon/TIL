콜백을 지우기위해 나타난 것 -> 프로미스

프로미스: 확실한 행동을 정해준다.



=========================================================

MVVM

----

Model

View 

ViewModel (vue) :  

MTV-MVC

---

SPA : single page application





---

<script src="node_modules/vue/dist/vue.js"></script>



​	data

​	template

​            methods

​            life cycle callback



​	filters

​            watch

​            coputed

​            methods

derective 

```
- vue 에서 제공하는 특수 속성임을 나타내는 V-접두어가 붙어있으며, 렌더링된 DOM에 특수한 반응형 동작을 한다.

- v-for / v-if / v-html / v-once
```

v-on:click - 디렉티브 바로뒤에 붙는 친구들을 전달인자라고 한다.

​	



binding : html에 뿌려주는 것

v-bind  html의 속성값에 사용 / 



v-model :  input, text, textarea

 form 에 관련된 태그에만 사용 될 수 있다.

---





2. 리스트 렌더링

v-for 

- 동일한 노드에 for와 if가 있다면 우선순위는 for가 높다. 즉 if는 for가 반복될때마다 실행된다.

---

3. 이벤트 리스너

v-on / @

v-on:전달인자.수식어

v-on:keyup.enter

---

4. 데이터 바인딩

   v-bind/ 생략

   v-model

5. 렌더링, 컴파일 관련

   v-pre

   v-once

   v-cloak

6. template element

   <template></template>







---

computed

미리 계산된 값을 반환

템플릿 내에 직접 로직을 넣을 수도 있지만, 그러면 템플릿이 너무 복잡해지기 때문에 vue 안에 정의해두는 것



### ==========================================================

input: 문자열

textarea: 문자열

단일 checkbox:boolean

다중 checkbox:array



### ==========================================================



Firebase



































