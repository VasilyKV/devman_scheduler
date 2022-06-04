"""
Этот модуль обрабатывает сценариии работы бота с сущностями БД
"""

# from datetime import datetime
import datetime
import os
import sys
import json

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


def fill_projects_db(json_file: str) -> None:
    with open(json_file, encoding='utf-8') as data:
        projects = json.load(data)
    for project in projects:
        Projects.objects.create(
            project_name=project['project_name'],
            project_start_date=datetime.fromisoformat(project['project_start_date']),
            project_end_date=datetime.fromisoformat(project['project_end_date'])
        )


def fill_students_db(json_file: str) -> None:
    with open(json_file, encoding='utf-8') as data:
        students = json.load(data)
    for student in students:
        Students.objects.create(
            std_name=student['name'],
            level=student['level'],
            std_tg_username=student['tg_username']
        )


def fill_pm_db(json_file: str) -> None:
    with open(json_file, encoding='utf-8') as data:
        product_managers = json.load(data)
    for product_manager in product_managers:
        ProductManagers.objects.create(
            pm_name=product_manager['name'],
            pm_tg_username=product_manager['tg_username']
        )


def conver_in_datetime(work_time: str): #format 18:20-20:00
    work_time_list = work_time.split('-')
    work_time_list[0] = datetime.datetime.strptime(work_time_list[0],'%H:%M')
    work_time_list[1] = datetime.datetime.strptime(work_time_list[1],'%H:%M')
    return work_time_list


def update_pm_db(pm_tg_username: str, pm_tg_id: int, work_time: str) -> None:
    work_time_splitted = conver_in_datetime(work_time)
    product_manager = ProductManagers.objects.get(pm_tg_username=pm_tg_username)
    product_manager.start_work_time = work_time_splitted[0]
    product_manager.end_work_time = work_time_splitted[1]
    product_manager.pm_tg_id = pm_tg_id # возможно integer не хватит
    product_manager.save()


def get_time_slots(start_period, end_period, slot_duration):
    time_slots = []
    slot = start_period
    timedelta = datetime.timedelta(minutes=slot_duration)
    while slot + timedelta <= end_period:
        time_slots.append(slot)
        slot += timedelta
    return (time_slots)


def fill_teams_db():
    index = 1
    product_managers = ProductManagers.objects.all()
    for product_manager in product_managers:
        time_slots = get_time_slots(product_manager.start_work_time, product_manager.end_work_time, 20)
        for time_slot in time_slots:
            Teams.objects.create(
                team_name=f'#{index}',
                pm_name=product_manager,
                time_slot=time_slot
            )
            index += 1

fill_teams_db()


def set_work_time_pm_db(): #Тестовая функция, заполняет поля времени в pm_db ,данные берет из доп поля  pm.json
    with open("pm.json", encoding='utf-8') as data:
        product_managers = json.load(data)
    for product_manager_json in product_managers:
        work_time_splitted = conver_in_datetime(product_manager_json['work_time'])
        product_manager_db = ProductManagers.objects.get(pm_name=product_manager_json['name'])
        product_manager_db.start_work_time = work_time_splitted[0]
        product_manager_db.end_work_time = work_time_splitted[1]
        product_manager_db.save()


#fill_pm_db("pm.json")
#fill_students_db("students.json")
#fill_projects_db("projects.json")

#update_pm_db('@vsmir',123,'18:20-20:20')

#set_work_time_pm_db()

# Students.objects.create(
#     std_name='Новый герой',
#     std_tg_id='777',
#     std_tg_username='@Новый герой',
#     level='junior',
#     wanted_time = ['18:30','20:30','21:30']
# )
# pm = ProductManagers.objects.all()[2]
# print(pm)
# a = datetime.datetime.strptime('18:30','%H:%M')
# Teams.objects.create(
#     team_name='Новая команда2',
#     pm_name=pm,
#     time_slot=a
# )
# a = datetime.datetime.strptime('18:30','%H:%M')
