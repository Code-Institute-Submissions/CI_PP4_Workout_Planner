# Generated by Django 3.2 on 2022-04-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plannerapp', '0013_alter_workoutplan_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workoutplan',
            name='first_day',
            field=models.DateField(),
        ),
    ]
