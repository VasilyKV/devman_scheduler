# devman_scheduler

## Для запуска
* Устанавливаем библиотеки `pip install -r pip_requirements.txt`
* Запускаем модуль `python main.py`
* Если изменили объекты в models.py,  нужно выполнить миграции в ДБ: `python manage.py makemigrations db; python manage.py migrate` 

### Настройка переменных окружения:
* Для хранения переменных окружения создаем файл .env:
```
touch .env
```
* Генерируем секретный ключ DJANGO:                                
1. `python`                                                        
2. `import django`                                                 
3. `from django.core.management.utils import get_random_secret_key`
4. `print(get_random_secret_key())`                                
5. Копируем строку в `.env` файл: 
`DJANGO_API_KEY='ваш ключ'`       

## Модуль main
Реализует сценарий обращений бота к объектам БД

## Модуль models в пакете db
Реализует саму бд
