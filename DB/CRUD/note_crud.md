### boorm

- 장점
  - 객체지향적인 코드로 인해 직관적이고 비즈니스로직에 더 집중할 수 있다.
  - 재사용 / 유지보수 증가
  - DB에 대한 종속성이 줄어듦



- 단점

  오로지  orm으로만은 거대한 서비스를 구현하기가 어렵다.

  어느정도 속도저하, orm을 거쳐 가기때문 (미비함)

```

```



##### SQLAlchemy datatype
##### Integer String Text DateTime Float Boolean







app.py 와 models.py를 나눠줘야함.

### ======================= models.py ========================

```python
#models.py  // DB모델을 만드는 곳, app과 분리해야 함.
# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):                
        return f"<User '{self.username}'>"
```

```
__repr__(self) : 프린트 출력형식을 바꿔줌
```

## ================== base.html ==================

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <!--블락태그는 파생된 템플릿이 변경할 수 있는 항목을 정의합니다.-->
    {% block head %}
    <!--파비콘 넣을 때 'static'폴더 만들고 그 안에 이미지를 가져와서 파비콘 설정-->
    <!--<link rel="icon" href="{{ url_for('static',filename='favicon.png' }}" type="image/png">-->
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %} - My webpage</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous"> 
    {% endblock %}
</head>

<body>
    <div class="container">
        <h1> base hi </h1>
        {% block body %} {% endblock %}

    </div>



    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>

</body>

</html>
```

```
{% block head %}{% endblock %}
=> 진자문법으로 해놓으면 상속받은 자식페이지에서 수정 가능한 부분

base를 만들고 한번에 적용
```

### ========================= app.py ==========================

```python
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User
app = Flask(__name__)

# flask app에 sqlalchemy 관련설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)


#뷰함수 / 보여주기 때문
@app.route('/')
def index():
    # url_for('index')=>>> '/'
    # 검색해서 users에 저장
    users = User.query.all()
    return render_template('index.html', users=users)

#얘는 페이지가 필요 없음. 작업하고 다시 보내줌
@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)
    
@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

## ================== index.html =====================

```python
<!--base를 가져 오는 것-->
{% extends "base.html" %}
{% block title %} INDEX {% endblock %}
{% block head %}
    <!--부모것을 가져 오겠다.-->
    {{ super() }}
    <!--추가하는 방법, 그냥 가져다 쓰면 위에것이 무시됨-->
    <!--<linsk rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">-->
{% endblock %}

{% block body %}
    <form action="/users/create">
        <input type="text" name="username"/>
        <input type="email" name="email"/>
        <input type="submit" name="Submit"/>
        
    </form>
    
    <ul>
        {% for user in users %}
            <li>
                저장완료    {{ user.username }} {{user.email}}
                <a href="/users/delete/{{ user.id }}"> [DELETE] </a>
                <a href="/users/edit/{{ user.id }}"> [EDIT] </a>
            </li>
            
        {% endfor %}
        
    </ul>
{% endblock %}
```

### =============== edit.html ==================================

```python
{% extends "base.html" %}
{% block body %}
    <h1>여기는 수정 페이지</h1>
    <form action="/users/update/{{ user.id }}">
        <input type="text" value="{{ user.username }}" name="username"/>
        <input type="text" value="{{ user.email }}" name="email"/>
        <input type="submit" name="Submit"/>
    </form>
{% endblock %}
```









### ========================================================

CREATE READ

DELETE

UPDATE (기존의 값을 불러온다음에 새로운 값 넣고 이걸 다시 넣어줘야)



