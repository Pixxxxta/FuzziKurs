# Generated by Django 4.0.4 on 2022-05-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('group', models.CharField(max_length=100, verbose_name='Группа')),
                ('result', models.IntegerField(verbose_name='Результат')),
            ],
        ),
    ]