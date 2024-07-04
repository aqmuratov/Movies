# Generated by Django 4.2 on 2024-07-04 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название фильма')),
                ('realised_date', models.DateField(verbose_name='Год выпуска')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('image', models.ImageField(upload_to='', verbose_name='Обложка фильма')),
                ('trailer', models.URLField(blank=True, null=True, verbose_name='Ссылка для трейлера')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.category')),
            ],
            options={
                'verbose_name': 'Фильмw',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
