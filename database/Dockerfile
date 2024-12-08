# Используем официальный образ PostgreSQL
FROM postgres:15

# Указываем переменную окружения для удобства
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=documents

# Копируем SQL-скрипты для инициализации
COPY init /docker-entrypoint-initdb.d/
