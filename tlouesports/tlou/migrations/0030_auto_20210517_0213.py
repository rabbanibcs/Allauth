# Generated by Django 3.2 on 2021-05-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlou', '0029_auto_20210511_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='crown',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.PositiveIntegerField(default=1200),
        ),
    ]
