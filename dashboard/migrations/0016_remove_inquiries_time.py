# Generated by Django 2.0.5 on 2018-07-17 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20180717_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiries',
            name='time',
        ),
    ]
