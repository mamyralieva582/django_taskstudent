# Generated by Django 5.0.5 on 2024-05-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('uptated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
                ('student', models.ManyToManyField(related_name='student', to='student.student', verbose_name='Студент')),
            ],
        ),
    ]
