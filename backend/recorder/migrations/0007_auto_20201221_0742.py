# Generated by Django 3.1.4 on 2020-12-21 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recorder', '0006_auto_20201221_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instantcontent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.recordeduser'),
        ),
    ]
