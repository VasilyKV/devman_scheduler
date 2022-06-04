from django.db import models



class ProductManagers(models.Model):
    pm_name = models.CharField(max_length=50)
    pm_tg_id = models.IntegerField(null=True)
    pm_tg_username = models.CharField(max_length=50)
    start_work_time = models.DateTimeField(null=True)
    end_work_time = models.DateTimeField(null=True)


class Students(models.Model):
    std_name = models.CharField(max_length=50)
    std_tg_id = models.IntegerField(null=True)
    std_tg_username = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    wanted_time = models.JSONField(null=True)


class Projects(models.Model):
    project_name = models.TextField()
    project_start_date = models.DateTimeField(null=True)
    project_end_date = models.DateTimeField(null=True)


class Teams(models.Model):
    team_name = models.TextField()
    pm_name = models.ForeignKey(ProductManagers, on_delete=models.CASCADE)
    students = models.JSONField()
    time_slot = models.DateTimeField(null=True)
    team_level = models.CharField(max_length=50)
    team_chat_username = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

