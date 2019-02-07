## D15 Workshop

#### 1.

```sqlite
CREATE TABLE bands (
id INTEGER PRIMARY KEY AUTOINCREMET,              
name TEXT
dubut INTEGER
)
```

​	- autoincrement 는 INTEGER에서만 사용 가능

```sql
SELECT id, name FROM bands;

SELECT name FROM bands WHERE debut < 2000;
```

