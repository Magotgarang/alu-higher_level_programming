-- creates a user and a password
CREATE USER IF NOT EXISTS 'user_0d_01'@'localhost';
ALTER USER 'user_0d_1'@'localhost' INDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * 'user_0d_1'@localhost;
FLUSH PRIVILEGES;
