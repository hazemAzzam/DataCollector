# Generated by Django 5.0.3 on 2024-04-08 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_recruit_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 23, 58, 41, 788232, tzinfo=datetime.timezone.utc)),
        ),
    ]