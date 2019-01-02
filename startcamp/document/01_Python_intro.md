
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Python-기초" data-toc-modified-id="Python-기초-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Python 기초</a></span><ul class="toc-item"><li><span><a href="#개요" data-toc-modified-id="개요-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>개요</a></span></li><li><span><a href="#식별자" data-toc-modified-id="식별자-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>식별자</a></span></li><li><span><a href="#기초-문법" data-toc-modified-id="기초-문법-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>기초 문법</a></span><ul class="toc-item"><li><span><a href="#인코딩-선언" data-toc-modified-id="인코딩-선언-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>인코딩 선언</a></span></li><li><span><a href="#주석(Comment)" data-toc-modified-id="주석(Comment)-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>주석(Comment)</a></span></li><li><span><a href="#코드-라인" data-toc-modified-id="코드-라인-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>코드 라인</a></span></li></ul></li></ul></li><li><span><a href="#변수(variable)-및-자료형" data-toc-modified-id="변수(variable)-및-자료형-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>변수(variable) 및 자료형</a></span><ul class="toc-item"><li><span><a href="#수치형(Numbers)" data-toc-modified-id="수치형(Numbers)-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>수치형(Numbers)</a></span><ul class="toc-item"><li><span><a href="#int-(정수)" data-toc-modified-id="int-(정수)-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span><code>int</code> (정수)</a></span></li><li><span><a href="#float(부동소수점,-실수)" data-toc-modified-id="float(부동소수점,-실수)-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span><code>float</code>(부동소수점, 실수)</a></span></li><li><span><a href="#complex-(복소수)" data-toc-modified-id="complex-(복소수)-2.1.3"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span><code>complex</code> (복소수)</a></span></li></ul></li><li><span><a href="#Bool" data-toc-modified-id="Bool-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Bool</a></span></li><li><span><a href="#None" data-toc-modified-id="None-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>None</a></span></li><li><span><a href="#문자형(String)" data-toc-modified-id="문자형(String)-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>문자형(String)</a></span><ul class="toc-item"><li><span><a href="#기본-활용법" data-toc-modified-id="기본-활용법-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>기본 활용법</a></span></li><li><span><a href="#이스케이프-문자열" data-toc-modified-id="이스케이프-문자열-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>이스케이프 문자열</a></span><ul class="toc-item"><li><span><a href="#깜짝-퀴즈" data-toc-modified-id="깜짝-퀴즈-2.4.2.1"><span class="toc-item-num">2.4.2.1&nbsp;&nbsp;</span>깜짝 퀴즈</a></span></li></ul></li><li><span><a href="#String-interpolation" data-toc-modified-id="String-interpolation-2.4.3"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>String interpolation</a></span></li></ul></li></ul></li><li><span><a href="#연산자" data-toc-modified-id="연산자-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>연산자</a></span><ul class="toc-item"><li><span><a href="#산술-연산자" data-toc-modified-id="산술-연산자-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>산술 연산자</a></span></li><li><span><a href="#비교-연산자" data-toc-modified-id="비교-연산자-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>비교 연산자</a></span></li><li><span><a href="#논리-연산자" data-toc-modified-id="논리-연산자-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>논리 연산자</a></span></li><li><span><a href="#복합-연산자" data-toc-modified-id="복합-연산자-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>복합 연산자</a></span></li><li><span><a href="#기타-연산자" data-toc-modified-id="기타-연산자-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>기타 연산자</a></span><ul class="toc-item"><li><span><a href="#Concatenation" data-toc-modified-id="Concatenation-3.5.1"><span class="toc-item-num">3.5.1&nbsp;&nbsp;</span>Concatenation</a></span></li><li><span><a href="#Containment-Test" data-toc-modified-id="Containment-Test-3.5.2"><span class="toc-item-num">3.5.2&nbsp;&nbsp;</span>Containment Test</a></span></li><li><span><a href="#Identity" data-toc-modified-id="Identity-3.5.3"><span class="toc-item-num">3.5.3&nbsp;&nbsp;</span>Identity</a></span></li><li><span><a href="#Indexing/Slicing" data-toc-modified-id="Indexing/Slicing-3.5.4"><span class="toc-item-num">3.5.4&nbsp;&nbsp;</span>Indexing/Slicing</a></span></li></ul></li><li><span><a href="#연산자-우선순위" data-toc-modified-id="연산자-우선순위-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>연산자 우선순위</a></span></li></ul></li><li><span><a href="#기초-형변환(Type-conversion,-Typecasting)" data-toc-modified-id="기초-형변환(Type-conversion,-Typecasting)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>기초 형변환(Type conversion, Typecasting)</a></span><ul class="toc-item"><li><span><a href="#암시적-형변환(Implicit-Type-Conversion)" data-toc-modified-id="암시적-형변환(Implicit-Type-Conversion)-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>암시적 형변환(Implicit Type Conversion)</a></span></li><li><span><a href="#명시적-형변환(Explicit-Type-Conversion)" data-toc-modified-id="명시적-형변환(Explicit-Type-Conversion)-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>명시적 형변환(Explicit Type Conversion)</a></span></li></ul></li><li><span><a href="#시퀀스(sequence)-자료형" data-toc-modified-id="시퀀스(sequence)-자료형-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>시퀀스(sequence) 자료형</a></span><ul class="toc-item"><li><span><a href="#list" data-toc-modified-id="list-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span><code>list</code></a></span></li><li><span><a href="#tuple" data-toc-modified-id="tuple-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span><code>tuple</code></a></span></li><li><span><a href="#range()" data-toc-modified-id="range()-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span><code>range()</code></a></span></li><li><span><a href="#시퀀스에서-활용할-수-있는-연산자/함수" data-toc-modified-id="시퀀스에서-활용할-수-있는-연산자/함수-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>시퀀스에서 활용할 수 있는 연산자/함수</a></span></li></ul></li><li><span><a href="#set,-dictionary" data-toc-modified-id="set,-dictionary-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>set, dictionary</a></span><ul class="toc-item"><li><span><a href="#set" data-toc-modified-id="set-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span><code>set</code></a></span></li><li><span><a href="#dictionary" data-toc-modified-id="dictionary-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span><code>dictionary</code></a></span></li></ul></li><li><span><a href="#정리" data-toc-modified-id="정리-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>정리</a></span><ul class="toc-item"><li><span><a href="#데이터-타입" data-toc-modified-id="데이터-타입-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>데이터 타입</a></span></li><li><span><a href="#Type-Conversion" data-toc-modified-id="Type-Conversion-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Type Conversion</a></span></li></ul></li></ul></div>

# Python 기초

## 개요

본 강의 자료는 [Python 공식 Tutorial](https://docs.python.org/3.6/tutorial/index.html)에 근거하여 만들어졌으며, Python 3.6버전에 해당하는 내용을 담고 있습니다.

또한, 파이썬에서 제공하는 스타일 가이드인 [`PEP-8`](https://www.python.org/dev/peps/pep-0008/) 내용을 반영하였습니다. 

파이썬을 활용하는 다양한 IT기업들은 대내외적으로 본인들의 스타일 가이드를 제공하고 있습니다. 

* [구글 스타일 가이드](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
* [Tensorflow 스타일 가이드](https://www.tensorflow.org/community/style_guide)

## 식별자

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다. 

* 식별자의 이름은 영문알파벳, \_, 숫자로 구성된다.
* 첫 글자에 숫자가 올 수 없다. 
* 대소문자를 구별한다.
* 아래의 예약어는 사용할 수 없다. 

```
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```


```python
import keyword
print(keyword.kwlist)
```

    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


*  내장함수나 모듈 등의 이름으로도 만들면 안된다.


```python
str='hi'
str(5)
```


    ---------------------------------------------------------------------------
    
    TypeError                                 Traceback (most recent call last)
    
    <ipython-input-3-c036f3861a0d> in <module>
          1 str='hi'
    ----> 2 str(5)


    TypeError: 'str' object is not callable



```python
# str() 형변환 함수로 정해진 식별자로 변수를 할당해버리면, 함수호출이 되지 않음.

```


```python
# 뒤에 코드에 영향이 가니까 변수를 메모리에서 지워줍시다!
del str

```

## 기초 문법

### 인코딩 선언

인코딩은 선언하지 않더라도 `UTF-8`로 기본 설정이 되어 있다. 

만약, 인코딩을 설정하려면 코드 상단에 아래와 같이 선언한다. 
주석으로 보이지만, Python `parser`에 의해 읽혀진다.


```python
# -*- coding: <encoding-name> -*- 
```

### 주석(Comment)

* 주석은 `#`으로 표현한다. 
* `docstring`은 `"""`으로 표현한다. 

   : 여러 줄의 주석을 작성할 수 있으며, 보통 함수/클래스 선언 다음에 해당하는 설명을 위해 활용한다.

* 예시 : flask 공식 문서 일부 발췌

![flask 공식문서 예시](./images/01/docstring.png)


```python
# 이 줄은 실행되지 않습니다.
def mysum(a,b):
    """이것은 덧셈 함수입니다.
    이 줄은 실행되지 않아요
    그런데 docstring인 이유가 있습니다.
    
    """
    print(a+b)
```


```python
mysum.__doc__
```




    '이것은 덧셈 함수입니다.\n    이 줄은 실행되지 않아요\n    그런데 docstring인 이유가 있습니다.\n    \n    '



### 코드 라인
* 기본적으로 파이썬에서는 `;` 을 작성하지 않는다.

* 한 줄로 표기할 떄는 `;`를 작성하여 표기할 수 있다. 


```python
print("hello")
print("ssafy")
```

    hello
    ssafy



```python
print("hello"); print("ssafy")
```

    hello
    ssafy



```python
a = 0
if a == 0:
    print(a)
```

    0


* 줄을 여러줄 작성할 때는 역슬래시`\`를 사용하여 아래와 같이 할 수 있다. 


```python
a = 0
if a == 0: 
    print(a)
```


```python
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

```

    |\_/|
    |q p|   /}
    ( 0 )"""\
    |"^"`    |
    ||_/=\\__|


* `[]` `{}` `()`는 `\` 없이도 가능하다.


```python

```

# 변수(variable) 및 자료형


<center><img src="./images/01/variable.png", alt="variable"/></center>


<center><img src="./images/01/box.png", alt="box"/></center>

* 변수는 `=`을 통해 할당(assignment) 된다. 

* 해당 자료형을 확인하기 위해서는 `type()`을 활용한다.

* 해당 변수의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.


```python

```

* 같은 값을 동시에 할당할 수 있다.


```python
x = y=1
print(x)
print(y)
```

    1
    1


* 다른 값을 동시에 할당 가능하다.


```python
x,y = 1, 2
print(x, y)

```

    1 2



```python
x, y = y, x
print(x, y)
```

    2 1



```python

```

* 이를 활용하면 서로 값을 바꾸고 싶은 경우 아래와 같이 활용 가능하다.


```python
# 쉽게 변수 값을 swap 가능함.

```

## 수치형(Numbers)

###  `int` (정수)

모든 정수는 `int`로 표현된다.

파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int` 형으로 표기 된다.

10진수가 아닌 8진수 : `0o`/2진수 : `0b` /16진수: `0x`로도 표현 가능하다. 


```python
a = 3
type(3)
```




    int




```python
# 보통 프로그래밍 언어 및 파이썬 2.x에서의 long은 OS 기준 32/64비트이다.
# 파이썬 3.x에서는 모두 int로 통합되었다.
a= 2**64
print(a)
```

    18446744073709551616



```python
import sys
max_int = sys.maxsize
print(max_int)
a = sys.maxsize * sys.maxsize
print(a)
```

    9223372036854775807
    85070591730234615847396907784232501249



```python
# 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형에서 오버플로우가 없다.
# arbitrary-precision arithmetic를 사용하기 때문이다. (메모리양이 정해져 있는 기존의 fixed-precision과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태) 

```


```python
# n진수
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexadecimal_number = 0x10
print(f'''
2진수 : {binary_number}
8진수 : {octal_number}
10진수 : {decimal_number}
16진수 : {hexadecimal_number}
''')
```

### `float`(부동소수점, 실수)

실수는 `float`로 표현된다. 

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않는다. (floating point rounding error)

이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있다.



```python
a = 3.5
type(a)
```




    float




```python
b = 314e-2
print(b)
```

    3.14



```python
3.5 + 3.2
```




    6.7




```python
3.5-3.12
```




    0.3799999999999999



* 실수의 경우 실제로 값을 처리하기 위해서는 조심할 필요가 있다.


```python
round(3.5 - 3.12,2)
```




    0.38




```python
0.1*3 == 0.3
```




    False




```python
a = 0.1*3
b = 0.3
abs(a-b ) < 10e-10
```




    True




```python
print (abs(a))
```

    0.30000000000000004



```python
import sys
abs(a-b) <= sys.float_info.epsilon

```




    True




```python
import math
math.isclose(a,b)
```




    True



* 따라서 다음과 같은 방법으로 처리 할 수 있다. 이외에 다양한 방법이 있음


```python
# 처리방법 1-1. 절대값을 비교

```


```python
# 처리방법 1-2. 절대값 비교를 내장된 float epsilon값과 비교

```


```python
# 처리방법 2. math 모듈을 통해 근사한 값인지 비교
# python 3.5부터는 math 모듈을 활용할 수 있다.

```

### `complex` (복소수)

복소수는 허수부를 `j`로 표현한다. 


```python
a=3 +4j
print(a.imag)
```

    4.0



```python
print(a.real)
```

    3.0



```python
# 허수 성분 얻기 (float)

# 실수 성분 얻기 (float)

# 켤레 복소수, 공액복소수 (허수 부분인 4j가 -4j가 된 수)

```

## Bool

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다.

비교/논리 연산을 수행 등에서 활용된다.

다음은 `False`로 변환됩니다.
```
0, 0.0, (), [], {}, '', None
```


```python
print(type(True))
```

    <class 'bool'>



```python
print(type(False))
```

    <class 'bool'>


* 형변환(Type Conversion)에서 추가적으로 다루는 내용입니다.


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

## None

파이썬에서는 값이 없음을 표현하기 위해 `None`타입이 존재합니다.


```python
print(type(None))
```

    <class 'NoneType'>



```python
a = None
print(None)
```

    None



```python

```

## 문자형(String)

### 기본 활용법

문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능하다. 

단, 문자열을 묶을 때 동일한 문장부호를 활용해야하며, `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하도록 하고 있습니다. 
(Pick a rule and Stick to it)


```python

```

* 다만 문자열 안에 문장부호(`'`, `"`)가 활용될 경우 이스케이프 문자(`\`)를 사용하는 것 대신 활용 가능 합니다. 


```python
print('철수가 말했다. '안녕?'')
```


      File "<ipython-input-1-4258189cde38>", line 1
        print('철수가 말했다. '안녕?'')
                          ^
    SyntaxError: invalid syntax




```python
print("철수가 말했다. '안녕?'")
print('철수가 말했다. \'안녕?\'')
```

    철수가 말했다. '안녕?'
    철수가 말했다. '안녕?'



```python
print("철수가 말했다. \"안녕?\"")
```

    철수가 말했다. "안녕?"



```python
print("\"안녕?\"")
```

    "안녕?"


* 여러줄에 걸쳐있는 문장은 다음과 같이 표현 가능합니다.

`PEP-8`에 따르면 이 경우에는 반드시 `"""`를 사용하도록 되어 있습니다.


```python
a = True
print(f"""물론,
아무거나 {a}""")
```

    물론,
    아무거나 True



```python
# string interpolation 도 가능합니다.

```

### 이스케이프 문자열

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다. 

|<center>예약문자</center>|내용(의미)|
|:--------:|:--------:|
|\n|줄바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|`\\`|`\`|
|\'|단일인용부호(')|
|\"|이중인용부호(")|


```python
print('이 다음은 엔터. \n그리고 \t (탭사이즈만큼 띄운다)')
print('나는 옆으로 쓰지요', end=" ")
print('이렇게')
print('개행 문자 말고도 가능합니다. 어떻게?', end="!!!!!a")
print('이러게')
```

    이 다음은 엔터. 
    그리고 	 (탭사이즈만큼 띄운다)
    나는 옆으로 쓰지요 이렇게
    개행 문자 말고도 가능합니다. 어떻게?!!!!!a이러게


* 이를 출력할 때 활용할 수가 있다.


```python

```


```python
\Windows\Users\내문서\Python
```

#### 깜짝 퀴즈

다음의 문장을 출력해보세요.

- `"""` 사용 금지
- `print` 여러번 사용 금지


```
"파일은 C:\Windows\Users\내문서\Python에 저장이 되어있습니다."
나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'
```


```python
# 여기에 코드를 작성해주세요.
#b = 'C:\Windows\Users\내문서\Python'
#print(f "\"파일은 {b}에 저장이 되어있습니다."\")
```


      File "<ipython-input-40-c058efe80375>", line 3
        print(f "\"파일은 {b}에 저장이 되어있습니다."\")
                                       ^
    SyntaxError: invalid syntax




```python
print("\"파일은 C:\Windows\\Users\\내문서\\Python에 저장이 되어있습니다.\"\n나는 생각했다. 'cd'를 써서 git bash로 들어가봐야지")
```

    "파일은 C:\Windows\Users\내문서\Python에 저장이 되어있습니다."
    나는 생각했다. 'cd'를 써서 git bash로 들어가봐야지



```python
print(" \"파일은\"")
```

     "파일은"


### String interpolation 

1) `%-formatting` 

2) [`str.format()` ](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

본 슬라이드에서는 `f-strings`의 기본적인 활용법만 알려드리고 나머지 `.format()`는 해당 [링크](https://pyformat.info/)에서 확인바랍니다.


```python
name = 'kaka'
'hello, {}'.format(name)
```




    'hello, kaka'




```python
f'hello, {name}'
```




    'hello, kaka'




```python
import datetime
today = datetime.datetime.now()
print(today)
```

    2019-01-02 15:42:28.237431



```python
f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%a}'
```




    '오늘은 19년 01월 02일 Wed'




```python
pi = 3.141592
f'원주율은 {pi:.3}, 반지름이 2일때 원의 넓이는 {pi*2*2}'
```




    '원주율은 3.14, 반지름이 2일때 원의 넓이는 12.566368'



* f-strings에서는 형식을 지정할 수 있으며,


```python
print(divmod(5,2))
a,b = divmod(5,2)
```

    (2, 1)



```python
positive_num = 4
print(-positive_num)
negative_num = -4
print(-negative_num)
```

    -4
    4


* 연산도 가능합니다.


```python
pi = 3.141592

```

# 연산자

## 산술 연산자
Python에서는 기본적인 사칙연산이 가능합니다. 

|연산자|내용|
|----|---|
|+|덧셈|
|-|뺄셈|
|\*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지(modulo)|
|\*\*|거듭제곱|



```python
3>6
```




    False




```python
3 != 3
```




    False




```python
3.0 == 3
```




    True




```python
# 내장함수 divmod()

```

* 양수/음수도 표현 가능합니다.


```python

```

## 비교 연산자

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

|연산자|내용|
|----|---|
|a > b|초과|
|a < b|미만|
|a >= b|이상|
|a <= b|이하|
|a == b|같음|
|a != b|같지않음|




```python

```


```python

```


```python

```


```python

```

## 논리 연산자

|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True|
|a or b|a 와 b 모두 False시만 False|
|not a|True -> False, False -> True|

우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자이다.


```python
print(not True)
print(not 0)
```

    False
    True



```python
# quiz! 답을 적어보고 실행하세요.
print(3 and 5)
print(0 and 3)
print(3 and 0)
print(0 and 0)
```

    5
    0
    0
    0



```python
# quiz! 답을 적어보고 실행하세요.
print(3 or 5)
print(0 or 3)
print(3 or 0)
print(0 or 0)
```

    3
    3
    3
    0


* 파이썬에서 and 는 a 가 거짓이면 a 를 리턴하고, 참이면 b 를 리턴한다.
* 파이썬에서 or 은 a 가 참이면 a 를 리턴하고, 거짓이면 b 를 리턴한다.


## 복합 연산자

복합 연산자는 연산과 대입이 함께 이뤄진다. 

가장 많이 활용되는 경우는 반복문을 통해서 갯수를 카운트하거나 할 때 활용된다.

|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|


```python
count = 0
while count<5:
    print(count)
    count += 1
    
```

    0
    1
    2
    3
    4


## 기타 연산자

### Concatenation

숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다.

### Containment Test

`in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

### Identity

`is` 연산자를 통해 동일한 object인지 확인할 수 있다. 


(나중에 Class를 배우고 다시 학습)

### Indexing/Slicing
`[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱 

(다음 챕터를 배우면서 추가 학습)


```python
print('kk')
```


```python
[1,2,3] + [4,5,6]
```




    [1, 2, 3, 4, 5, 6]




```python
'a' in 'apple'
```




    True




```python
1 in [2,3,4]
```




    False




```python
5 in range(1,8)
```




    True




```python
a = 100006
b = 100006
print(a is b)
print(a == b)
```

    False
    True



```python
a = 3
b = 3
a is b
```




    True




```python
def animal():
    cat = 10006
    print(cat is 10006)   # 같은함수에서는 동일한 메모리를 사용
animal()
```

    True



```python
a = '나라사랑나는너다고다이곧이알지이어만'
b = '나라사랑나는너다고다이곧이알지이어만'
a is b
```




    False




```python
'hello'[0] # 표현법 신기
```




    'h'




```python
3**2/2+8*3/2
```




    16.5




```python

```

## 연산자 우선순위

0. `()`을 통한 grouping

1. Slicing

2. Indexing

3. 제곱연산자
    \*\*

4. 단항연산자 
    +, - (음수/양수 부호)

5. 산술연산자
    \*, /, %
    
6. 산술연산자
    +, -

7. 비교연산자, `in`, `is`

8. `not`

9. `and` 

10. `or`


```python

```

# 기초 형변환(Type conversion, Typecasting)


파이썬에서 데이터타입은 서로 변환할 수 있다.

## 암시적 형변환(Implicit Type Conversion)
사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우이다.
아래의 상황에서만 가능하다.
* bool
* Numbers (int, float, complex)


```python
True + 3
```




    4




```python
int_num = 3
float_num = 5.0
complex_num = 3 + 5j
print(int_num + float_num)
print(type(int_num + float_num))   # 우선순위를 정하여 암시적 형변환
```

    8.0
    <class 'float'>



```python
print(float_num + complex_num)
print(type(float_num + complex_num))
```

    (8+5j)
    <class 'complex'>



```python

```

## 명시적 형변환(Explicit Type Conversion)

위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야한다.

* string -> intger  : 형식에 맞는 숫자만 가능
* integer -> string : 모두 가능

암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능하다.

* `int()` : string, float를 int로 변환
* `float()` : string, int를 float로 변환
* `str()` : int, float, list, tuple, dictionary를 문자열로 변환

`list(), tuple()` 등은 다음 챕터에서 배울 예정이다.


```python
# integer와 string 사이의 관계는 명시적으로 형변환을 해줘야만 한다.

```


```python
str(1) + '등'
```




    '1등'




```python
a= '3.5'
float(a)
```




    3.5




```python

```


```python
# string은 글씨가 숫자일때만 형변환이 가능하다.

```


```python
# string 3.5를 int로 변환할 수는 없다.

```


```python
# float 3.5는 int로 변환이 가능하다.

```


```python
a = 3.5
int(a)
```




    3




```python
print(int('55')+3)
print('55'+str(3))     #문자열을 합함
```

    58
    553


# 시퀀스(sequence) 자료형

`시퀀스`는 데이터의 순서대로 나열된 형식을 나타낸다. 

**주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.**

파이썬에서 기본적인 시퀀스 타입은 다음과 같다.

1. 리스트(list)

2. 튜플(tuple)

3. 레인지(range)

4. 문자열(string)

5. 바이너리(binary) : 따로 다루지는 않습니다.



## `list`

<center><img src="./images/01/list.png", alt="list figure"/></center>

**활용법**
```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 를 통해 만들 수 있습니다.

값에 대한 접근은 `list[i]`를 통해 합니다.


```python
L = []
print(type(L))
```

    <class 'list'>



```python
location = ['서울','대전','광주','구미']
print(location)
```

    ['서울', '대전', '광주', '구미']



```python

```

## `tuple`

**활용법**
```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

그리고 tuple은 수정 불가능(immutable)하고, 읽을 수 밖에 없습니다.

직접 사용하는 것보다는 파이썬 내부에서 사용하고 있습니다.


```python


# 아래와 같이 만들 수 있습니다.
tuple_ex = (1,2)
print(type(tuple_ex))

is_tuple = 1,2,4
print(is_tuple)
```

    <class 'tuple'>
    (1, 2, 4)



```python
# 파이썬 내부에서는 다음과 같이 활용됩니다.
# 앞선 2. 변수 및 자료형 예제에서 사용된 코드입니다.
x,y = 1,2
print(x)
print(y)
```

    1
    2



```python
x, y = 'sss', 'ttt'
print(x)
x,y = y,x
print(x)
```

    sss
    ttt



```python
# 아래의 변수의 값을 swap하는 코드 역시 tuple을 활용하고 있습니다. 

```

##  `range()`

레인지는 숫자의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : `range(n)` 


> 0부터 n-1까지 값을 가짐


범위 지정 : `range(n, m)` 

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다


```python
type(range(1))
```




    range




```python
list(range(10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(4,9))
```




    [4, 5, 6, 7, 8]




```python
list(range(0,-10,-1))
```




    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]




```python

```


## 시퀀스에서 활용할 수 있는 연산자/함수 

|operation|설명|
|---------|---|
|x in s	|containment test|
|x not in s|containment test|
|s1 + s2|concatenation|
|s * n|n번만큼 반복하여 더하기
|s[i]|indexing|
|s[i:j]|slicing|
|s[i:j:k]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 갯수|


```python
# contain test
s = 'string'
print('a' in s)
```

    False



```python
# concatenation
L = [1,2,3,6,7]
print(3 in L)
```

    True



```python
print('안녕'+'하세요.')
print([1,2] + [4,5])
```

    안녕하세요.
    [1, 2, 4, 5]



```python
# indexing과 slicing
location = ['a','b','c','d']
location[1]
```




    'b'




```python
location[1:3]  # 사이기준으로 생각 - > 슬라이싱
```




    ['b', 'c']




```python
r = list(range(30))
print(r[0:30:3])
print(r[0:len(r):3])
```

    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]



```python
# 기타 내장함수
len(r)
```


```python
L = [1,2,1,1,2,3]
L.count(1)
```




    3




```python

```


```python

```

# set, dictionary

* `set`과 `dictionary`는 기본적으로 순서가 없습니다.

## `set`

세트는 수학에서의 집합과 동일하게 처리됩니다. 

세트는 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없습니다.

**활용법**
```python
{value1, value2, value3}
```

|연산자/함수|설명|
|---|---|
|a \| b|합집합|
|a & b|교집합|
|a - b|차집합|
|a.union(b)|합집합|
|a.intersection(b)|교집합|
|a.difference(b)|차집합|


```python
# 이렇게 만들어서 쓸 것
set_a = set()
print(type(set_a))
set_a = {1,2,3}
set_b = {3,6,9}
print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
```

    <class 'set'>
    {1, 2, 3, 6, 9}
    {3}
    {1, 2}



```python
set_c = (1,2,3)
print(type(set_c))
set_c = set((1,2,3))
print(type(set_c))
```

    <class 'tuple'>
    <class 'set'>


* `set`을 활용하면 `list`의 중복된 값을 손쉽게 제거할 수 있습니다.


```python
list_a = [1,2,3,1,2,3]
set(list_a)
```




    {1, 2, 3}




```python
list(set(list_a))
```




    [1, 2, 3]




```python

```


```python
1 in list_a
```




    True



## `dictionary`

<center><img src="./images/01/dictionary.png"/></center> 

**활용법**
```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

* 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조입니다. 
* `{}`를 통해 만들며, `dict()`로 만들 수도 있습니다.
* `key`는 immutable한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
* `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.


```python
dict_a={}  # 선언방법
print(type(dict_a))
```

    <class 'dict'>



```python
phone_book = {"서울": "02", "대전":"042"}
phone_book["서울"]
```




    '02'




```python
# 중복된 key는 존재할 수가 없습니다.
phone_book = {"서울": "02", "대전":"042","서울":"115"}  # 마지막 키값으로 대체됨.
print(phone_book)
```

    {'서울': '115', '대전': '042'}



```python
# 딕셔너리의 메소드를 활용하여 key와 value를 확인 해볼 수 있습니다.
phone_book.keys()   # 객체로 나온다.
```




    dict_keys(['서울', '대전'])




```python
phone_book.items()
print(type(phone_book.items()))
```

    <class 'dict_items'>



```python
phone_book.values()
```




    dict_values(['115', '042'])




```python
# 실습! 친구 전화번호부 딕셔너리를 작성해주세요.
```

# 정리
## 데이터 타입
<center><img src="./images/01/container.png", alt="container"/></center>

## Type Conversion
<center><img src="./images/01/typecasting.png", alt="typecasting"/></center>
