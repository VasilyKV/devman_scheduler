from django.db import models
from django.db.models.fields import DateTimeField, IntegerField

class Projects(models.Model):
    name = models.CharField(max_length=100)
    date_start = DateTimeField()
    date_end = DateTimeField()


class Product_managers(models.Model):
    name = models.CharField(max_length=50)
    tg_id = IntegerField()
    tg_nick = models.CharField(max_length=50)
    time_slot = models.DateTimeField()


class Students(models.Model):
    name = models.CharField(max_length=50)
    tg_id = IntegerField()
    level = models.IntegerField()
    time_slot = models.DateTimeField()


class Teams(models.Model):
    team_id = models.TextField
    pm_tg_name = models.CharField(max_length=100)
    pm_name = models.ForeignKey(Product_managers, on_delete=models.CASCADE)  # pm=Product_managers.name
    students = models.JSONField()  # В это поле кладем JSON с учениками
    time = models.ForeignKey(Students, on_delete=models.CASCADE)
    level = IntegerField()  
