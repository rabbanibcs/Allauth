# Generated by Django 3.1.7 on 2021-04-12 10:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlou', '0007_auto_20210410_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media/Banner')),
                ('content', ckeditor.fields.RichTextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
    ]
