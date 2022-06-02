# Generated by Django 4.0.5 on 2022-06-02 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tg_id', models.IntegerField()),
                ('tg_nick', models.CharField(max_length=50)),
                ('time_slot', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tg_id', models.IntegerField()),
                ('level', models.IntegerField()),
                ('time_slot', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm_tg_name', models.CharField(max_length=100)),
                ('students', models.JSONField()),
                ('level', models.IntegerField()),
                ('pm_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.product_managers')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.students')),
            ],
        ),
    ]