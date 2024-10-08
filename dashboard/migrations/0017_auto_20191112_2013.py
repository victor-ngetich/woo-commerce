# Generated by Django 2.2.7 on 2019-11-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_inquiries_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.CharField(blank=True, choices=[('Advertising Services', 'Advertising'), ('Automotive Services', 'Automotive'), ('Beauty Services', 'Beauty'), ('Car Rental Services', 'Car Rental'), ('Catering Services', 'Catering'), ('Cleaning Services', 'Cleaning'), ('Computer & IT Services', 'Computer'), ('Event Planning', 'Event'), ('Fitness Services', 'Fitness'), ('Interior Design', 'Interior Design'), ('Logistics Services', 'Logistics'), ('Massage Therapy', 'Massage Therapy'), ('Pet Services', 'Pet'), ('Photography & Video Services', 'Photography & Video'), ('Real Estate Services', 'Real Estate'), ('Renovation Services', 'Renovation'), ('Repair Service', 'Repair'), ('Travel Agencies', 'Travel Agencies'), ('Web Design Services', 'Web Design'), ('Wedding Services', 'Wedding'), ('Others', 'Others')], max_length=255, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='services',
            name='payment_info',
            field=models.CharField(default='Mpesa Paybill Number: 914226, Account Number:Name of Service Porvider', max_length=255),
        ),
    ]
