## D16 Workshop

```sqlite
CREATE TABLE bands(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
debut INTEGER
);

INSERT into bands
VALUES
('Queen', 1973, 4),
('Coldplay', 1998, 5),
('MCR', 2001, 9);

UPDATE bands SET members=5 WHERE id=3;

DELETE FROM bands WHERE id=2;
```

