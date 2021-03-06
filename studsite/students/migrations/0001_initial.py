# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Код группы')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Starosta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.Group')),
            ],
            options={
                'verbose_name': 'Староста',
                'verbose_name_plural': 'Старосты',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('student_ID', models.IntegerField(verbose_name='Номер студенческого')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Group')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.AddField(
            model_name='starosta',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]
