### 0131

network 7 layers - 기초

---

객체 / 딕셔너리 



model view controller

DB

get : url 창에 보인다.

post : 보이지 않는다. 하지만 보안X

---

- ## ping pong _ POST방식

  #### ping 에서 name을 달아서 pong으로 넘김, 

  #### 이때 route를 통해서 다시 pong으로 뿌려준다.

  #### pong에서는 받아온 값을 출력해준다.

```python
@app.route("/ping_new")
def ping_new():
    return render_template('ping_new.html')

@app.route("/pong_new", methods=["POST"])
def pong_new():
    user = request.form['q']
    return render_template('pong_new.html', html_user = user)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/pong_new" method="POST">
        <input type="text" name="q"/>
        <input type="submit" value="Submit"/>
        
    </form>
    
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h2> 여기는 뉴퐁</h2>
    <h2>{{ html_user }}</h2>
</body>
</html>
```





- ## csv writer _ reader

  1. timeline에서 입력한 값을 get으로 받는다. / 이때 딕셔너리 비슷한 형태의 객체이다.
  2. 받아온 값을 Dictwriter로 읽어서 csv파일에 저장한다.

  ```
  파일열기모드
  r : 읽기모드 - 읽기만 할 때
  w : 쓰기모드 - 파일에 내용을 쓸 때 (새롭게 쓰임)
  a : 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
  ```

  3. 읽어올 때는 DictReader를 통해 한줄 씩 가져온다.
  4. for문을 통해 순서대로 저장한다.
  5. 저장한 형태(여기서는 리스트)를 timeline.html로 쏘아준다.
  6.  페이지에서 출력한다.

```python
import csv
@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
        
    #DictWriter 'timeline.csv'
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message') # 미리 넣어둔 필드네임들
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'username':username, 'message':message})
    
     
    return render_template('timeline_create.html',username=username, message=message)
    

    @app.route('/timeline')
def timeline():
    with open('timeline.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        temp=[]
        for row in reader:
            temp.append((row['username'],row['message']))
    
    return render_template('timeline.html', temp = temp)
```

### ==========================================================

# 데이터베이스

- 사캠에서 정리해볼 것