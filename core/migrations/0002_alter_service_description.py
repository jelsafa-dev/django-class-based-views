# Generated by Django 3.2.12 on 2022-02-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
    ]
