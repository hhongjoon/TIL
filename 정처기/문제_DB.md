#### 정규화 과정

```
도메인이 원자값 			1NF 조건
부분적 함수 종속 제거		2NF
이행적 함수 종속 제거		3NF
결정자이면서 후보키 아닌 것 제거 BCNF
다치종속						4NF
조인종속성 이용				5NF

```



\16. SQL은 사용 용도에 따라 DDL, DML, DCL 로 구분할 수 있다. 다음 중 성격이 다른 하나는?

​    ① UPDATE  ② ALTER

​    ③ DROP  ④ CREATE

```
 DDL : CREATE, ALTER, DROP
 DML : SELECT, DELETE, UPDATE, INSERT
 DCL : GRANT, REVOKE, COMMIT, ROLLBACK
```






\2. 관계형 대수의 연산자가 아닌 것은?

   ① JOIN  ② PROJECT

   ③ PRODUCT  ④ PART

```
관계형 대수 : 테이블을 조작
 
집합 연산자(수학에서 사용) 
 합집합(union), 교집합 (intersection), 차집합 (difference), 프로덕트 (product)

특수 연산자(테이블에만 적용) 
 selection, projection, join, division
```



\5. 해싱에서 동일한 홈 주소로 인하여 충돌이 일어난 레코드들의 집합을 의미하는 것은?

   ① Overflow  ② Bucket

   ③ Synonym  ④ Collision

```
 ㆍ오버플로우(Overflow) : 버킷에 더 이상의 레코드를 보관할 수 없는 상태이다.
 ㆍ버킷(Bucket) : 하나의 주소를 갖는 파일의 한 구역을 의미하며, 버킷의 크기는 같은 주소에 포함될 수 있는 레코드 수이다.
 ㆍ충돌(Collision) : 레코드를 삽입할 때 2개의 상이한 레코드가 똑같은 홈 주소로 해싱되는 경우이다.


 동일한 주소 충돌 = COLLISION
 충돌 레코드 집합 = SYNONYM 
```



\4. SQL View(뷰)에 대한 설명으로 틀린 것은?

   ① 뷰(View)를 제거하고자 할때는 DROP 문을 이용한다.

   ② 뷰(View)의 정의를 변경하고자 할때는 ALTER 문을 이용한다.

   ③ 뷰(View)를 생성하고자 할때는 CREATE 문을 이용한다.

   ④ 뷰(View)의 내용을 검색하고자 할때는 SELECT 문을 이용한다.

<문제 해설>
 뷰는 변경이 안되므로 삭제후 (DROP->CREATE)로 다시 재 생성해야 합니다.

변경X



\5. 다음 설명에 해당하는 스키마는?

​     ![img](file:///C:\Users\박재원\AppData\Local\Temp\Hnc\BinData\EMB000009686465.gif)  

   ① conceptual schema  ② internal schema

   ③ external schema  ④ definition schema

<문제 해설>

 외부 스키마(External Schema) : 프로그래머나 사용자의 입장에서 데이터베이스의 모습으로 조직의 일부분을 정의한 것

 개념 스키마(Conceptual Schema) : 모든 응용 시스템과 사용자들이 필요로하는 데이터를 통합한 조직 전체의 데이터베이스 구조를 논리적으로 정의한 것

 내부 스키마(Internal Schema) : 전체 데이터베이스의 물리적 저장 형태를 기술하는 것



\6. 데이터베이스 내에서 데이터들이 불필요하게 중복되어 릴레이션 조작시 예기치 못한 곤란한 현상을 무엇이라고 하는가?

   ① Normalization ② Bug

   ③ Anomaly  ④ Error

<문제 해설>
 이상(anomaly) 현상
 데이터의 중복으로 인해 릴레이션을 처리할때 발생하는 곤란한 현상
 데이터 베이스 사용자의 의도와는 다르게 다른데이터가 삽입 삭제 갱신되는 현상



\9. 관계데이터 모델의 무결성 제약 중 기본키 값의 속성 값이 널(null)값이 아닌 원자 값을 갖는 성질은?

   ① 개체 무결성  ② 참조 무결성

   ③ 도메인 무결성 ④ 튜플의 유일성

<문제 해설>
 개체 무결성 : 릴레이션에서 기본키를 구성하는 속성은 널(NULL)값이나 중복값을 가질 수 없음을 의미합니다.

참조 무결성 : 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야한다는 의미입니다, 즉 릴레이션은 참조할 수 없는 외래키 값을 가질 수 없습니다.

도메인 무결성 : 특정 속성의 값이 그 속성이 정의된 도메인에 속한 값이어야 한다는 규정입니다.

튜플의 유일성 : 무결성 제약 조건에 해당하지 않는 보기입니다.



NoSQL : 단순검색



14. 관계 대수에 대한 설명으로 옳지 않은 것은?

​    ① 릴레이션을 처리하기 위한 연산의 집합으로 피연산자가 릴레이션이고 결과도 릴레이션이다.

​    ② 원하는 정보와 그 정보를 어떻게 유도하는가를 기술하는 절차적 특징을 가지고 있다.

​    ③ 일반 집합 연산과 순수 관계 연산이 있다.

​    ④ 수학의 Predicate Calculus 에 기반을 두고 있다.

<문제 해설>
 관계대수 : 절차적 언어 / 순수 관계 연산(select, project, join, division)과 일반 집합연산(union, intersection, difference, cartesian product) 
 관계해석 : 비절차적 언어 / Predicate Calculus에 기반을 둠    / 튜플 및 도메인 관계해석
 [해설작성자 : sdk]

 관계대수(릴레이션 조작을 위한 연산의집합.기술적인특성)의 순수관계 연산자
 - 릴레이션을 처리하기 위한 연산의 집합으로 피연산자가 릴레이션이고 결과도 릴레이션이다.
 - Select : 수평적 부분집합. 시그마를 사용
 - Project : 수직적 부분집합. 파이를 이용
 - Join
 - Division : 두 릴레이션 A,B에 대해 릴레이션의 모든 조건을 만족하는 튜플들을 릴레이션 A에서 분리해 내어 프로젝션 함.

 보기 4의 Predicate Calculus에 기반을 두고있다는 관계해석에 대한 설명이다..<-



\15. 데이터베이스 로그(log)를 필요로 하는 회복 기법은?

​    ① 즉각 갱신 기법

​    ② 대수적 코딩 방법

​    ③ 타임 스탬프 기법

​    ④ 폴딩 기법

<문제 해설>
 데이터베이스 로그(log)를 필요로 하는 회복 기법의 종류
 1. 연기 갱신 기법(Deferred Update)
 2. 즉각 갱신 기법(Immediate Update)
 3. 그림자 페이지 대체 기법(Shadow Paging)
 4. 검사점 기법(Check Point)
 

 회복(recovery)
 -트랜잭션들을 수행하는 도중 장애로 인해 손상된 데이터베이스를 손상되기 이전의 정상적인 상태로 복구시키는 작업.

 - 회복 기법의 종류로는
          1. Deferred Modification(연기 갱신 기법)
          2. Immediate Update(즉각 갱신 기법)
          3. Shadow Paging(그림자 페이지 대체 기법)
          4.  Check Point(검사점 기법)

