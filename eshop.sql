--sqlite3
-- create table products(id, title, price)

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price INTEGER
);

INSERT INTO products(title, price) VALUES
('iPhone', 1000),
('Samsung', 800),
('Xiaomi', 600),
('Huawei', 500),
('Nokia', 400),
('Sony', 300),
('LG', 200),
('HTC', 100);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT
);

INSERT INTO users(username, email) VALUES
('John', 'XXXXXXXXXXXXXX'),
('Bob', 'XXXXXXXXXXXXXX'),
('Mike', 'XXXXXXXXXXXXXX'),
('Alex', 'XXXXXXXXXXXXXX'),
('Ann', 'XXXXXXXXXXXXXX');

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT
);

INSERT INTO articles(title, author) VALUES
('Article 1', 'John'),
('Article 2', 'Bob'),
('Article 3', 'Mike');