# Generated by Django 3.1.7 on 2021-04-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlou', '0016_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='ladders',
            name='maxmembers',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='ladders',
            name='minmembers',
            field=models.IntegerField(default=1),
        ),
    ]
