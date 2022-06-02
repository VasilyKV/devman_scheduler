"""
Этот модуль обрабатывает сценариии работы бота с сущностями БД
"""

from datetime import datetime
import os
import sys

import django



sys.dont_write_bytecode = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

"""
------------------------------------------------------------------------------
Ниже можем реализовывать разные сценарии работы бота с БД
------------------------------------------------------------------------------
"""


"""Заказчик анонсирует проект"""
Projects.objects.create(
    project_name='Автоматизация формирования групповых проектов',
    project_start_date=datetime.fromisoformat('2022-05-13'),
    project_end_date=datetime.fromisoformat('2022-05-20')
)


"""Бот проводит опрос продукт-менеджеров"""
ProductManagers.objects.create(
    pm_name='Игорь Суровый',
    pm_tg_id=54322381,
    pm_tg_username='@igsu',
    start_work_time=datetime.fromisoformat('2022-05-13 20:00'),
    end_work_time=datetime.fromisoformat('2022-05-13 22:00')
)


ProductManagers.objects.create(
    pm_name='Василий Смирнов',
    pm_tg_id=5432238123423,
    pm_tg_username='@vsmir',
    start_work_time=datetime.fromisoformat('2022-05-13 18:00'),
    end_work_time=datetime.fromisoformat('2022-05-13 21:00')
)


ProductManagers.objects.create(
    pm_name='Петр Непервый',
    pm_tg_id=54322342345111,
    pm_tg_username='@1petr',
    start_work_time=datetime.fromisoformat('2022-05-13 17:00'),
    end_work_time=datetime.fromisoformat('2022-05-13 20:00')
)


"""
Бот проводит опрос студентов
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
"""
