# Generated by Django 4.2.6 on 2023-10-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationbox',
            name='main_text',
            field=models.TextField(max_length=5000),
        ),
    ]