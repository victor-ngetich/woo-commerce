# Generated by Django 2.0.5 on 2018-07-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_inquiries_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiries',
            name='booked_time',
            field=models.DateField(default='2018-07-20'),
        ),
    ]
