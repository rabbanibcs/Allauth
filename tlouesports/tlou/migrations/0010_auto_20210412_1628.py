# Generated by Django 3.1.7 on 2021-04-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlou', '0009_auto_20210412_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='rank',
        ),
        migrations.AlterField(
            model_name='banner',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
