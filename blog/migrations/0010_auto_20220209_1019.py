# Generated by Django 3.2.9 on 2022-02-09 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220209_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='start_date',
        ),
    ]
