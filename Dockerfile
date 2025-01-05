# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем скрипт в контейнер
COPY generate_password.py /app/

# Указываем команду для выполнения скрипта
CMD ["python", "generate_password.py"]
