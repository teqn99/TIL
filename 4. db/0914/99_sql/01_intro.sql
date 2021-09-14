-- 주석
/* SQL 구문은 대소문자가 중요하지 않다.(구분x)
    기본 문법 (변하지 않는 부분 - 대문자)
    변하는 부분 - 소문자
 */
 -- 데이터 전체 조회 SELECT
SELECT * FROM examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- 테이블 삭제
DROP TABLE classmates;

-- 연습
CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- 데이터 입력
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

SELECT * FROM classmates;

-- 모든 열에 데이터가 있는 경우, 컬럼을 명시하지 않아도 된다.
INSERT INTO classmates VALUES ('홍길순', 40, '서울');

-- PK가 따로 없으면, 자동으로 rowid를 만들어 생성하고 있다.
SELECT rowid, * FROM classmates;

-- 테이블 삭제
DROP TABLE classmates;


CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES (1, '홍길순', 40, '서울');
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '제주');

SELECT * FROM classmates;

DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 데이터 입력
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
INSERT INTO classmates VALUES
('김길동', 30, '서울'),
('박길동', 30, '서울'),
('장길동', 30, '서울'),
('정길동', 30, '서울'),
('이길동', 30, '서울');

SELECT * FROM classmates;

SELECT rowid, * FROM classmates;


SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates;

DELETE FROM classmates WHERE rowid=5;


UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=2;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INT NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INT NOT NULL
);

SELECT * FROM users WHERE age >= 30;
SELECT age, last_name FROM users WHERE age >= 30 and last_name='김';

SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age>=30;
SELECT MAX(balance), first_name FROM users;
SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02%';
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;


CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번 내용');
SELECT * FROM articles;
ALTER TABLE 