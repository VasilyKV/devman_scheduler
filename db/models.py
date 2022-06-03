from django.db import models



class ProductManagers(models.Model):
    pm_name = models.CharField(max_length=50)
    pm_tg_id = models.IntegerField()
    pm_tg_username = models.CharField(max_length=50)
    start_work_time = models.DateTimeField()
    end_work_time = models.DateTimeField()


class Students(models.Model):
    std_name = models.CharField(max_length=50)
    std_tg_id = models.IntegerField()
    std_tg_username = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    wanted_time = models.JSONField()


class Projects(models.Model):
    project_name = models.TextField()
    project_start_date = models.DateTimeField()
    project_end_date = models.DateTimeField()


class Teams(models.Model):
    team_name = models.TextField()
    pm_name = models.ForeignKey(ProductManagers, on_delete=models.CASCADE)
    students = models.JSONField()
    time_slot = models.DateTimeField()
    team_level = models.CharField(max_length=50)
    team_chat_username = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

