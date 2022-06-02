from datetime import datetime
import sys
import os

import django


sys.dont_write_bytecode = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Product_managers, Projects, Students 

"""Закакзчик анонсирует проект"""
Projects.objects.create(
    name='Автоматизация формирования групповых проектов',
    date_start=datetime.fromisoformat('2022-05-13'),
    date_end=datetime.fromisoformat('2022-05-20'),
)

"""Бот проводит опрос продукт-менеджеров"""
Product_managers.objects.create(
    name='Игорь Суровый',
    tg_id=54322381,
    tg_nick='igsu',
    time_slot=datetime.fromisoformat('2022-05-20 20:00'),
)

"""Бот проводит опрос студентов"""
Students.objects.create(
    name='Вася Петров',
    tg_id=35789213,
    level=1,
    time_slot=datetime.fromisoformat('2022-05-20 20:00'),

)
Students.objects.create(
    name='Владимир Иванов',
    tg_id=3578923243,
    level=1,
    time_slot=datetime.fromisoformat('2022-05-20 20:00'),

)
Students.objects.create(
    name='Олеся Какаято',
    tg_id=35789213,
    level=1,
    time_slot=datetime.fromisoformat('2022-05-20 20:00'),


)

