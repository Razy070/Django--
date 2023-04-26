# Generated by Django 4.2 on 2023-04-24 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_salary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='tovar',
            options={'ordering': ('-created',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование категории товаров'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка на категорию товаров'),
        ),
        migrations.AlterField(
            model_name='tovar',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Ссылка на товар'),
        ),
        migrations.AlterField(
            model_name='tovar',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование товара'),
        ),
    ]
