# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем последнюю версию pip
RUN pip install --upgrade pip

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем Python-зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшийся код
COPY . .

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
