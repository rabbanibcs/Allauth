# Generated by Django 3.1.7 on 2021-04-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlou', '0010_auto_20210412_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(null=True, upload_to='media/Banner'),
        ),
    ]
