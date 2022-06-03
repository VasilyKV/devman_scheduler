"""
Этот модуль обрабатывает сценариии работы бота с сущностями БД
"""

from datetime import datetime
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
    with open(json_file) as data:
        projects = json.load(data)
    for project in projects:
        Projects.objects.create(
            project_name=project['project_name'],
            project_start_date=datetime.fromisoformat(project['project_start_date']),
            project_end_date=datetime.fromisoformat(project['project_end_date'])
        )


def fill_students_db(json_file: str) -> None:
    with open(json_file) as data:
        students = json.load(data)
    for student in students:
        Students.objects.create(
            std_name=student['std_name'],
            std_tg_id=student['std_tg_id'],
            std_tg_username=student['std_tg_username'],
            level=student['level'],
        )


def fill_pm_db(json_file: str) -> None:
    with open(json_file) as data:
        product_managers = json.load(data)
    for product_manager in product_managers:
        ProductManagers.objects.create(
            pm_name=product_manager['pm_name'],
            pm_tg_id=product_manager['pm_tg_id'],
            pm_tg_username=product_manager['pm_tg_username'],
        )


def update_pm_db(pm_tg_username: str, work_time_splitted: list[str]) -> None:
    product_manager = ProductManagers.objects.get(pm_tg_username=pm_tg_username)
    product_manager.start_work_time = datetime.fromisoformat(work_time_splitted[0])
    product_manager.end_work_time = datetime.fromisoformat(work_time_splitted[1])
    product_manager.save()


"""
update_pm_db(
    pm_tg_username="@vsmir", 
    work_time_splitted=["2019-03-02 20:00", "2019-03-02 22:00"]
)
"""

# fill_pm_db("pm.json")
# fill_students_db("students.json")
# fill_projects_db("projects.json")

