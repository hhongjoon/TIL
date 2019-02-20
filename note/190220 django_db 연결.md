### 190220 django_ db 연결



- 앱 추가시 해야할 것

```bash
1. original app 에서 urls.py 에서 뿌려주기
2. 새로만든 앱에 url.py 추가
===================  DB연걸  ====================
3 models.py 에서 class 생성
    # migration 파일 생성
    python manage.py makemigrations '이름'  
    # migrate 적용
    python manage.py migrate '이름'
    #마이그레이션 적용 현황
    python manage.py sqlmigrate '이름' '마이그레이션-이름'

```









## --------------------------------------

settings.py 에 DATABASES 에서 사용 데이타베이스 설정가능

``` bash
# migration 파일 생성
python manage.py makemigrations '이름'  
# migrate 적용
python manage.py migrate '이름'
#마이그레이션 적용 현황
python manage.py sqlmigrate '이름' '마이그레이션-이름'

sqlite3 db.sqlite3
python manage.py shell
    
    
 11  pip install django-extensions
   12  python manage.py shell_plus       # import 필요 X
   
   python manage.py createsuperuser
   
```



```

```









```bash
from boards.models import Board
Board.objects.all()

>>> board = Board()
>>> board.title = 'first'
>>> board.content = 'django!'
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>]>
# 한줄 짜리 객체


Board.objects.create(title='third', content='django!!!')  # 저장필요 X 알아서 딤
board.full_clean()  # 확인가능

>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>


# 차이점 알 것
>>> Board.objects.filter(title='first').all()
<QuerySet [<Board: 1: first>]>
>>> Board.objects.filter(title='first').first()
<Board: 1: first>

>>> board = Board.objects.get(pk=1)     # key 가져올때만 사용할 것

#차이점 볼 것
>>> board = Board.objects.get(pk=1)
>>> board
<Board: 1: first>
>>> board = Board.objects.filter(id=1)
>>> board
<QuerySet [<Board: 1: first>]>

# 내림차순 오름차순
boards = Board.objects.order_by('title').all()
>>> boards = Board.objects.order_by('-title').all()
>>> boards
<QuerySet [<Board: 3: third>, <Board: 2: second>, <Board: 4: fourth>, <Board: 1: first>]>

board = Board.objects.get(pk=1)
>>> board.title = 'hello'
>>> board.save()
>>> board
<Board: 1: hello>
>>> board.delete()
(1, {'boards.Board': 1})
```







.tables

.schema boards_board





{{ board.created_at|timesince }} 전
        {{ board.created_at }}