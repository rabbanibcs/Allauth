# Generated by Django 3.1.7 on 2021-04-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlou', '0006_userdtl'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdtl',
            name='psn',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='userdtl',
            name='xbl',
            field=models.CharField(default='', max_length=500),
        ),
    ]
