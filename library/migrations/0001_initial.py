# Generated by Django 5.1.6 on 2025-02-20 07:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('profile', models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на профиль')),
                ('is_deleted', models.BooleanField(default=False, help_text='True - пользователь удален. Он не будет отображаться на сайте', verbose_name='Удален')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'unique_together': {('firstname', 'lastname', 'birth_date')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('publish_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, choices=[('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction'), ('science fiction', 'Science Fiction'), ('fantasy', 'Fantasy'), ('mystery', 'Mystery'), ('biography', 'Biography')], max_length=50, null=True)),
                ('pages', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='library.category', verbose_name='Category ID')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('library_url', models.URLField(blank=True, max_length=100, null=True)),
                ('books', models.ManyToManyField(blank=True, null=True, related_name='libraries', to='library.book')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=50, verbose_name='Пол')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('age', models.IntegerField()),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('employee', 'Employee'), ('reader', 'Reader')], max_length=50, verbose_name='Роль')),
                ('is_active', models.BooleanField(default=True)),
                ('libraries', models.ManyToManyField(related_name='members', to='library.library')),
            ],
            options={
                'unique_together': {('name', 'surname', 'birth_date')},
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publish_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.member'),
        ),
    ]
