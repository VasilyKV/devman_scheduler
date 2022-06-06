"""
Этот модуль обрабатывает сценариии работы бота с сущностями БД
"""

# from datetime import datetime
import datetime
import os
import sys
import json

import django
from django.db.models import Q


sys.dont_write_bytecode = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

"""
------------------------------------------------------------------------------
Ниже можем реализовывать разные сценарии работы бота с БД
------------------------------------------------------------------------------
"""
slot_duration = 30

def fill_projects_db(json_file: str) -> None:
    with open(json_file, encoding='utf-8') as data:
        projects = json.load(data)
    for project in projects:
        Projects.objects.create(
            project_name=project['project_name'],
            project_start_date=datetime.fromisoformat(
                project['project_start_date']),
            project_end_date=datetime.fromisoformat(
                project['project_end_date'])
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


def range_conver_in_datetime(work_time: str):  # format 18:20-20:00
    work_time_list = work_time.split('-')
    work_time_list[0] = datetime.datetime.strptime(work_time_list[0], '%H:%M')
    work_time_list[1] = datetime.datetime.strptime(work_time_list[1], '%H:%M')
    return work_time_list


def time_slots_conver_in_datetime(time_slots):  # format [18:20, 20:00]
    time_slots_datetime = []
    for slot in time_slots:
        time_slots_datetime.append(datetime.datetime.strptime(slot, '%H:%M'))
    return time_slots_datetime


def get_time_slots(start_period, end_period, slot_duration):
    time_slots = []
    slot = start_period
    timedelta = datetime.timedelta(minutes=slot_duration)
    while slot + timedelta <= end_period:
        time_slots.append(slot)
        slot += timedelta
    return (time_slots)


def range_convetr_to_slots_list(time_range):
        work_time_splitted = range_conver_in_datetime(time_range)
        time_slots = get_time_slots(work_time_splitted[0], work_time_splitted[1], slot_duration)
        list_slots = []
        for slot in time_slots:
            list_slots.append(slot.strftime('%H:%M'))
        return(list_slots)


def update_pm_db(pm_tg_username: str, pm_tg_id: str, work_time: str) -> None:
    try:
        product_manager = ProductManagers.objects.get(
            pm_tg_username=pm_tg_username)
    except ProductManagers.DoesNotExist:
        print("product_manager isn't in the database yet")
        return
    work_time_splitted = range_conver_in_datetime(work_time)
    product_manager.start_work_time = work_time_splitted[0]
    product_manager.end_work_time = work_time_splitted[1]
    product_manager.pm_tg_id = pm_tg_id
    product_manager.save()


def fill_teams_db():
    index = 1
    product_managers = ProductManagers.objects.all()
    for product_manager in product_managers:
        time_slots = get_time_slots(
            product_manager.start_work_time, product_manager.end_work_time, slot_duration)
        for time_slot in time_slots:
            Teams.objects.create(
                team_name=f'#{index}',
                pm_name=product_manager,
                time_slot=time_slot
            )
            index += 1


def get_free_slots(tg_username):
    free_slots = []
    try:
        student = Students.objects.get(std_tg_username=tg_username)
    except Students.DoesNotExist:
        print("Student isn't in the database yet")
        return free_slots

    teams_sorted = Teams.objects.filter(Q(team_level=None) | Q(
        team_level=student.level)).order_by('time_slot')
    if teams_sorted:
        time_slot = datetime.datetime.strptime('00:00', '%H:%M')
        for team in teams_sorted:
            if team.students_name:
                team_incomplited = len(team.students_name) < 3
            else:
                team_incomplited = True
            if (team.time_slot != time_slot) & team_incomplited:
                time_slot = team.time_slot
                free_slots.append(time_slot.strftime('%H:%M'))
    return free_slots  # format [18:20, 20:00]


def update_students_db(tg_username: str, tg_id: str, time_slots):
    try:
        student = Students.objects.get(std_tg_username=tg_username)
    except Students.DoesNotExist:
        print("Student isn't in the database yet")
    student.std_tg_id = tg_id
    # student.wanted_time = time_slots # Это строчка должна работать когда приходит список слотов
    student.wanted_time = range_convetr_to_slots_list(time_slots)
    student.save()


def update_teams_db():
    students_sorted = Students.objects.filter(team_id=None, wanted_time__isnull=False).order_by(Length('wanted_time').asc())
    teams_sorted = Teams.objects.order_by('time_slot')
    for student in students_sorted:
        for team in teams_sorted:
            if student.team_id: break
            if team.students_name:
                team_incomplited = (len(team.students_name) < 3)
            else:
                team_incomplited = True
            print(student.std_name,team.team_name, team_incomplited, team.team_level, student.level)
            if ((team.team_level == None) or (team.team_level == student.level)) & team_incomplited:
                print('-',student.std_name,team.team_name, team_incomplited, team.team_level, student.level)
                for slot in student.wanted_time:
                    if slot == team.time_slot.strftime('%H:%M'):
                        student.team_id = team
                        team.team_level = student.level                    
                        if team.students_name:
                            team.students_name.append(student.std_name)
                        else:
                            team.students_name = [student.std_name]
                        student.save()
                        team.save()
                        break


def set_work_time_pm_db():  # Тестовая функция, заполняет поля времени в pm_db ,данные берет из доп поля  pm.json
    with open("pm.json", encoding='utf-8') as data:
        product_managers = json.load(data)
    for product_manager_json in product_managers:
        work_time_splitted = range_conver_in_datetime(
            product_manager_json['work_time'])
        product_manager_db = ProductManagers.objects.get(
            pm_name=product_manager_json['name'])
        product_manager_db.start_work_time = work_time_splitted[0]
        product_manager_db.end_work_time = work_time_splitted[1]
        product_manager_db.save()


def set_work_time_student_db():  # Тестовая функция, заполняет поля времени в Students_db ,данные берет из доп поля  students.json
    with open("students.json", encoding='utf-8') as data:
        students = json.load(data)    
    for student_json in students:
        student_db = Students.objects.get(std_name=student_json['name'])
        student_db.wanted_time = range_convetr_to_slots_list(student_json['work_time'])
        student_db.save()

# -------Рабочие функции------

#fill_pm_db("pm.json")
#fill_students_db("students.json")
#fill_projects_db("projects.json")
#fill_teams_db()
#update_teams_db()

#--------Тестовые функции-----
# set_work_time_pm_db()
# set_work_time_student_db()
# update_pm_db('@vsmir',333,'19:00-20:20')
# update_students_db('@masha', 5555, '18:30-20:30')

#--------Мусор для отладки-----

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

# team.team_level='novice+'
# team.students_name=['Сидоров']
# team.students_name.append('Сидоров_3')
# team.save()

# slots = ['19:00', '19:30', '21:00']


# teams = Teams.objects.all()
# for team in teams:
#     print(team.team_name, team.team_level,team.time_slot, team.students_name)
