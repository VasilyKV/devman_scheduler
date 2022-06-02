from django.db import models


class Product_managers(models.Model):
    name = models.CharField(max_length=50)
    tg_id = models.BigIntegerField
    time_slot = models.DateTimeField


class Students(models.Model):
    name = models.CharField(max_lenth=50)
    tg_id = models.BigIntegerField
    level = models.IntegerField
    time_slot = models.DateTimeField


class Teams(models.Model):
    team_id = models.TextField
    pm = models.ForeignKey(Product_managers, on_delete=None) # pm=Product_managers.name
    students = models.JSONField()  # В это поле кладем JSON с учениками
    time = models.ForeignKey(Students, on_delete=None)
    level = models.ForeignKey(Students, on_delete=None)
