# Generated by Django 3.1.4 on 2020-12-24 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recorder', '0010_auto_20201222_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instantcontent',
            name='user',
        ),
    ]