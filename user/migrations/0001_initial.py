# Generated by Django 4.1.1 on 2022-10-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('username', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
        ),
    ]
