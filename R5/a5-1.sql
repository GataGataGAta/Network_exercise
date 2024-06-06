.open a5-1.db
.mode box
DROP TABLE IF EXISTS events;
CREATE TABLE events(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date DATE, place TEXT);
INSERT INTO events(name, date, place) VALUES('シドニーオリンピック','2000-08-01','オーストラリア');
INSERT INTO events(name, date, place) VALUES('アテネオリンピック','2004-08-02','ギリシャ');
INSERT INTO events(name, date, place) VALUES('北京オリンピック','2008-08-03','中国');
INSERT INTO events(name, date, place) VALUES('ロンドンオリンピック','2012-08-04','イギリス');
INSERT INTO events(name, date, place) VALUES('リオオリンピック','2016-08-05','ブラジル');
INSERT INTO events(name, date, place) VALUES('東京オリンピック','2020-08-06','日本');
INSERT INTO events(name, date, place) VALUES('パリオリンピック','2024-08-07','フランス');
INSERT INTO events(name, date, place) VALUES('ロスオリンピック','2028-08-08','アメリカ');
INSERT INTO events(name, date, place) VALUES('ブリスベンオリンピック','2032-08-09','オーストラリア');
INSERT INTO events(name, date, place) VALUES('エジプトオリンピック','2036-08-10','エジプト');
.mode column
SELECT * FROM events;
SELECT * FROM events WHERE name LIKE '%アテネ%';
SELECT * FROM events WHERE date > CURRENT_DATE;
SELECT * FROM events WHERE date < CURRENT_DATE;