# Generated by Django 5.0.6 on 2024-06-18 10:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_categoryvacancy_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryvacancy',
            name='title_ky',
            field=models.CharField(max_length=123, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='categoryvacancy',
            name='title_ru',
            field=models.CharField(max_length=123, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_ky',
            field=models.CharField(max_length=123, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_ru',
            field=models.CharField(max_length=123, null=True, verbose_name='Название'),
        ),
    ]
