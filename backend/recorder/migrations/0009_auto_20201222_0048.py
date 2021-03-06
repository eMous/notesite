# Generated by Django 3.1.4 on 2020-12-22 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recorder', '0008_auto_20201221_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='instantcontent',
            name='compressionMethod',
            field=models.IntegerField(choices=[(1, 'gzip')], null=True),
        ),
        migrations.AddField(
            model_name='instantcontent',
            name='content',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='instantcontent',
            name='textVersionContent',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='instantcontent',
            name='contentType',
            field=models.IntegerField(choices=[(1, 'Text & Image'), (2, 'Location'), (3, 'Voice')]),
        ),
        migrations.AlterField(
            model_name='instantcontent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.recordeduser'),
        ),
    ]
