# Generated by Django 3.2.9 on 2022-02-09 10:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220209_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 2, 9, 10, 23, 18, 294761, tzinfo=utc)),
            preserve_default=False,
        ),
    ]