# Generated by Django 3.1.5 on 2021-03-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab09', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(unique=True),
        ),
    ]