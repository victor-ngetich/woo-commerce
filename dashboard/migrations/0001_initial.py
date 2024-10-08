# Generated by Django 2.0.5 on 2018-07-07 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiries',
            fields=[
                ('Client_name', models.CharField(max_length=255)),
                ('client_email', models.EmailField(blank=True, max_length=254)),
                ('created_at', models.DateTimeField()),
                ('order_number', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('attachment', models.FileField(upload_to='dashboard/')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('cellphone', models.IntegerField(blank=True, default=1)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
