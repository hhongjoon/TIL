INSERT INTO users(username, email)
VALUES ('junho','example@gmail.com');

user = User(username='junho', email='example@gmail.com')

SELECT * FROM users;
users = User.query.all()

SELECT * FROM users WHERE username = 'junho';
users = User.query.filter_by(username='junho').all()

SELECT * FROM users WHERE username='junho' LIMIT 1;
users = User.query.filter_by(username='junho').first()
-- miss
miss = User.query.filter_by(username='ssafy').first()


-- 프라이머리 키만 GET으로 가져올 수 있음.
SELECT * FROM users WHERE id = 1;
user = User.query.get(1)

-- LIKE
user = User.query.filter(User.email.like('%exam%')).all()

-- UPADATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
