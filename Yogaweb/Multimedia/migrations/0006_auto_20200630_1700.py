# Generated by Django 3.0.7 on 2020-06-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Multimedia', '0005_auto_20200628_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_list',
            name='VideoFile',
            field=models.FileField(upload_to='videos-list'),
        ),
    ]
