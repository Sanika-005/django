# Generated by Django 3.2.9 on 2022-02-09 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='timestamp',
        ),
    ]