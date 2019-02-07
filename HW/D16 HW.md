## D16 HW



#### 1.

```sqlite
CREATE TABLE friends(
id INTEGER;
name TEXT;
location TEXT;
)

INSERT INTO friends
VALUES(1,Justin, Seoul);
VALUES(2,Simon, New York);
VALUES(3,Chang, Las Vegas);
VALUES(4,John, Sydney);

ALTER TABLE friends
ADD COLUMN married INTEGER;

UPDATE friends SET location="LA", married=1 WHERE id=1
UPDATE friends SET married=0 WHERE id=2
UPDATE friends SET married=0 WHERE id=3
UPDATE friends SET married=1 WHERE id=4

DELETE from friends WHERE marrid = 0;



```



