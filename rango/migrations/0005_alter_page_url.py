# Generated by Django 5.0.1 on 2024-02-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
