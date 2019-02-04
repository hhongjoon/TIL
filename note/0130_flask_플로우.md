### 0130 _ 프론트 플로우

1. img 마우스 오버시 손가락으로 변경
2. favicon
3. 대문사진 필터
4. card 높이 균일하게
5. 평점 뱃지 정렬 깨지지 않게

---

- 명세서를 보고 container가 몇개 필요할지 생각
- 순서 맞출 것
- modal 연결 할 때 위치를 카드 안에 넣어야 가독성 증가
- target 할 때 숫자로 시작하면 연결 X
- namig 할 때 구체적으로해야 다음에 찍을 수 있음. (백엔드와 같이 할 때 매우 중요)



---

1. 프로그래밍 폰트

2. web 프로젝트 정리

3. gitlab

4. flask c9 setting

   ```python
   from flask import Flask, render_template
   import os
   import datetime
   from datetime import timedelta
   app = Flask(__name__)
   
   @app.route('/')
   def index():
       return 'hello there!'
   ```


```
https://gist.github.com/edujunho/bee20c196ecacc3e8cdf068b4ec64d9f

들어가서

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
pyenv rehash

를 입력하면 파이썬 설치

이후

git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

엔터

다음에

pyenv virtualenv 3.6.7 test-venv

입력

이후
pyenv virtualenvs

입력

이후

pyenv local test-venv

입력


이것을 입력하는 이유는
독립된 공간을 만들기 위해서

가상환경에서 나가고 싶으면

pyenv uninstall test-venv
pyenv-virtualenv: remove /home/ubuntu/.pyenv/versions/3.6.7/envs/test-venv?  ----> y
```



5. flask datetime

   ```
   flask에서 return 할 때는 str만 가능
   ```

6. flask variable routing

   ```python
   @app.route('/hi/<string:name>')
   def greeting(name):
       # return f"안녕{name}"
       return render_template('greeting.html', html_name = name)
   ```

7. render template

8. flask 조건반복

   ```html
   {%if post in moives%}
   	<h2>{{post}}</h2>
   {%else%}
   	<h2>not{{post}}</h2>
   {%endif%}
   ```