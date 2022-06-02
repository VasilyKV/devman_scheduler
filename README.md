# devman_scheduler

## Для запуска
* Устанавливаем библиотеки `pip install -r pip_requirements.txt`
* Запускаем модуль `python main.py`
* Если изменили объекты в models.py,  нужно выполнить миграции в ДБ: `python manage.py makemigrations db; python manage.py migrate` 

## Модуль main
Реализует сценарий обращений бота к объектам БД

## Модуль models в пакете db
Реализует саму бд
