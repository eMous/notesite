# Generated by Django 3.1.4 on 2020-12-18 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InstantContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentType', models.IntegerField(choices=[(1, 'Text & Image'), (2, 'Location'), (3, 'Voice')])),
            ],
        ),
        migrations.CreateModel(
            name='UploadingFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InstantContentDraft',
            fields=[
                ('instantcontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recorder.instantcontent')),
            ],
            bases=('recorder.instantcontent',),
        ),
    ]
