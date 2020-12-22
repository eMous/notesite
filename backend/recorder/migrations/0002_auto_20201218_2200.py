# Generated by Django 3.1.4 on 2020-12-18 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recorder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kk', models.IntegerField(default=12)),
            ],
        ),
        migrations.AlterField(
            model_name='instantcontent',
            name='contentType',
            field=models.IntegerField(choices=[(1, 'Text & Image'), (2, 'Location'), (3, 'Voice')], null=True),
        ),
        migrations.AddField(
            model_name='instantcontent',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recorder.manufacturer'),
        ),
    ]
