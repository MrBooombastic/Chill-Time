# Generated by Django 4.2.6 on 2023-11-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyquote',
            name='day',
            field=models.DateField(),
        ),
    ]
