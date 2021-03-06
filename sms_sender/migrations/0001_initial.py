# Generated by Django 3.1.7 on 2021-03-04 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Отчество')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='Телефон должен быть в формате +996[код][номер]', regex='^(\\+996)\\d{9}$')], verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Сообщение (комментарий)')),
                ('file', models.ImageField(blank=True, null=True, upload_to='files', verbose_name='Файл')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
