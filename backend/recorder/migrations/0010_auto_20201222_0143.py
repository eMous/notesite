# Generated by Django 3.1.4 on 2020-12-22 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recorder', '0009_auto_20201222_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='downloadUrl',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='uploadAs',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='record',
            name='browserName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='deviceName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='deviceType',
            field=models.IntegerField(choices=[(1, 'PC'), (2, 'Mac'), (3, 'Android Phone'), (4, 'iPhone'), (5, 'iPad')], null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='gpsLat',
            field=models.DecimalField(decimal_places=7, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='gpsLon',
            field=models.DecimalField(decimal_places=7, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='other',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='softwareName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='softwareVersion',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='timeZone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='uploadingfile',
            name='uploadingDir',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='instantcontent',
            name='contentType',
            field=models.IntegerField(choices=[(1, 'Text & Image'), (2, 'Location'), (3, 'Voice')], null=True),
        ),
        migrations.AlterField(
            model_name='instantcontent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recorder.recordeduser'),
        ),
    ]
