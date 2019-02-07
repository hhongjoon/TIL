import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User
app = Flask(__name__)

# flask app에 sqlalchemy 관련설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ['SQLALCHEMY_TRACK_MODIFICATIONS'] True/sqlachemy 데이터베이스 객체 수정 및 신호 방출 등을 추적합니다. 과도한 메모리 사용이라서 False

# sqlalchemy 초기화
# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app,db)
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
    
#     def __repr__(self):
#         return f"<User '{self.username}'>"
        
# 실행방법
# flask db init
# flask db migrate
# flask db upgrade

#뷰함수 / 보여주기 때문
@app.route('/')
def index():
    # url_for('index')=>>> '/'
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