.open books.db
.mode box
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    published_date TEXT NOT NULL
);
INSERT INTO books (title, author, published_date) VALUES
('Pythonプログラミング', '山田 太郎', '2022-01-15'),
('フラスク入門', '佐藤 花子', '2023-03-22'),
('データベース設計', '鈴木 一郎', '2021-07-30');
.mode column
