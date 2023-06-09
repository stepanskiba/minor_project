# Generated by Django 4.2.2 on 2023-06-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlgoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='1007. Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. Определить, поместится ли жидкость объёма M в первую ёмкость, во вторую, в обе.', max_length=255, verbose_name='Формулировка задачи')),
                ('A', models.IntegerField(default=0, verbose_name='Ребро куба')),
                ('H', models.IntegerField(default=0, verbose_name='Высота цилиндра')),
                ('R', models.IntegerField(default=0, verbose_name='Радиус цилиндра')),
                ('M', models.IntegerField(default=0, verbose_name='Обьем жидкости')),
                ('current_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения(save)')),
            ],
            options={
                'verbose_name': 'A_H_R_M',
                'verbose_name_plural': 'A_H_R_M_S',
                'ordering': ('-id', '-M'),
            },
        ),
    ]
