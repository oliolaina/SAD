# Используем Node.js базовый образ
FROM node:16

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем package.json и устанавливаем зависимости
COPY package.json ./
RUN npm install

# Копируем остальной код
COPY . ./

# Запускаем React-приложение
CMD ["npm", "start"]
RUN npm run build

# Публикуем порт для взаимодействия
EXPOSE 3000
