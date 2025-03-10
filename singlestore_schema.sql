CREATE DATABASE transactions_db;

USE transactions_db;

CREATE TABLE transactions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    account VARCHAR(255),
    amount DOUBLE,
    type ENUM('debit', 'credit', 'transfer'),
    timestamp DATETIME DEFAULT NOW()
) PARTITION BY HASH(account);
