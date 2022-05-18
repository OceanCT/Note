CREATE DATABASE jdbc;

USE jdbc;

CREATE TABLE users(
		id INT PRIMARY KEY AUTO_INCREMENT, -- id主键
		name VARCHAR(40)  unique  NOT NULL, --账户名称，设置不为空
		password VARCHAR(40) NOT NUll -- 密码，设置不为空

) CHARACTER SET utf8 COLLATE utf8_general_ci;

INSERT INTO users(NAME,PASSWORD,email,birthday) VALUES('zs','123456');
INSERT INTO users(NAME,PASSWORD,email,birthday) VALUES('lisi','123456');
INSERT INTO users(NAME,PASSWORD,email,birthday) VALUES('wangwu','123456');
