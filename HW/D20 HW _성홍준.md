D20 HW _성홍준

1. #### Django는 요청에 대한 응답을 해줄 때 허용하는 도메인에게만 응답을 해주도록 설정한다. Settings.py 파일에서 도메인을 허용하기 위해 수정해줘야 하는 변수이름을 찾아서 적어주세요

   ```
   ALLOWED_HOSTS에 주소를 추가해준다. => 허용해야지 들어가진다.
   
   
   
   
   INSTALLED_APPS =[ 'home.apps.HomeConfig' ]
   
   이런식으로 
   ```

   

2. #### https:///ssafy 로 요청이 들어왔을때 응답을 해주기 위해 urls.py에 추가해주어야 할 코드를 작성하세요 (실행하는 함수는 views.py 안에 있는 ssafy 함수라고 가정한다.)

  ```python
  path('ssafy/', views.ssafy, name='ssafy'),
  #ssafy/ 주소로 들어왔을때 views.ssafy로 넘겨준다.
  ```

  

3. #### Django 서버를 실행시키는 명령어를 작성해주세요 (C9환경에서)

   ```
   django-admin startproject django_intro .   # 장고프로젝트 만들 때 명령어
   python manage.py runserver $IP:$PORT       # 서버 실행
   ```

   

4. #### django는 MTV로 이루어진 web framework 이다. MTV가 무엇의 약자인지 작성하세요

  ```
  Model
  - 데이터 서비스를 제공하는 Layer이다. Home밑에 models.py 안에 정의한다. 하나 이상의 모델 클래스를 정의할 수 있으며, 모델클래스는 데이타베이스에서 하나의 테이블에 해당된다.
  
  Template
  - HTML 파일로서 Home 폴더 밑에 'templates'를 만들고 .html 을 넣는다.
  
  View
  - View는 필요한 데이터를 Model에서 가져와서 웹페이지에 결과를 보여주는 컨트롤러 역할이다.
  ```

  

