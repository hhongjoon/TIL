### 0123 _ 스크래핑 복습

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('가져올 태그 주소').text    # soup.select('') 역시 가능
print(kospi)
```

```python
import requests
from bs4 import Beautifulsoup

url = 'www..w.w..w'
req = requests.get(url).text    # url의 값을 가져옴
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#___').text
```

### pprint 사용

```python
from pprint import pprint
```





## ==================================================





#### LGEB 파이썬  _ 정의된 위치에 따라서 스코프 범위가 달라진다.

####  			_ 지역변수에 변수가 없을 시 global 설정을 해주어야 접근 가능. 

Local = 함수 내 정의된 지역 변수

Enclosing Function local = 함수를 내포하는 또 다른 함수 영역

Global = 함수영역에 포함되지 않는 모듈영역

Built-in = 내장영역



#### python _ call by assignment         

#####     //  value도 아니고 reference 도 아니다. 하지만 쓰이긴함



# ======================================

>https://stackshare.io/stackups

```html
alt shift f  => 코드정리
alt b            => 바로 창을 띄워줌
alt w
open in browser => 단축키로 창 띄우는  확장 프로그램
htmltagwrap

span 태그?

bootstrap 기본 저장해야 할 태그

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">


<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>


cssreset.com

```

