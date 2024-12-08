FROM nginx:latest

# Создаём директорию для сертификатов
RUN mkdir -p /etc/nginx/certs

# Генерируем самоподписанный сертификат
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/certs/localhost.key \
    -out /etc/nginx/certs/localhost.crt \
    -subj "/CN=localhost"

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Открываем порты для HTTP и HTTPS
EXPOSE 80 443
