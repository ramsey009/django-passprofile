# Generated by Django 3.1.3 on 2020-11-11 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0008_user_raw_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='raw_password',
        ),
    ]
