# Generated by Django 3.1.5 on 2021-02-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll_no', models.IntegerField()),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]
