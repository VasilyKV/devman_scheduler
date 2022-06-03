# devman_scheduler

## Запуск:
### 1. Устанавливаем библиотеки:
```
pip install -r pip_requirements.txt
```

### 2. Для хранения переменных окружения создаем файл .env:
```
touch .env
```
Генерируем секретный ключ DJANGO в интерактивном режиме python:
    1. `python`
    2. `import django`
    3. `from django.core.management.utils import get_random_secret_key`
    4. `print(get_random_secret_key())`
    5. Копируем строку в `.env` файл: `DJANGO_KEY='ваш ключ'`    

### 3. Выполняем миграции в ДБ: 
```
python manage.py makemigrations db; python manage.py migrate
``` 
### 4. Запускаем модуль:
```
python main.py
```

## Модуль main
Реализует сценарий обращений бота к объектам БД

## Модуль models в пакете db
Реализует саму бд
