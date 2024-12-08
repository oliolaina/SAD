-- Создание таблицы пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Создание таблицы документов
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    sender_id INTEGER NOT NULL REFERENCES users(id),
    receiver_id INTEGER NOT NULL REFERENCES users(id)
);
