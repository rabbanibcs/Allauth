# Generated by Django 3.2.5 on 2021-07-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='dc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='ld',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='pr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
