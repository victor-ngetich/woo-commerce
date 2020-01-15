from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
import string
import random

# Create your models here.
class Inquiries(models.Model):
	MAYBECHOICE = (
    ('Paid',1),
    ('Unpaid',0),
   )
	client_name = models.CharField(max_length=255,blank=True)
	client_email = models.EmailField(blank=True)
	cellphone = models.CharField(max_length=25, blank=True)
	order_number = models.AutoField(primary_key=True)
	created_at = models.DateTimeField()
	user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=2)
	message = models.CharField(max_length=255,blank=True)	
	transaction_code = models.CharField(max_length=255,blank=True)
	payment_status = models.BooleanField(max_length=6, choices=MAYBECHOICE,default=1)
	booked_time = models.DateField(blank=False,default="2018-07-20")
	def __unicode__(self):
		return self.Client_name


class services(models.Model):
	MAYBECHOICE2 = (
    ('Advertising','Advertising'),
    ('Automotive','Automotive'),
	('Beauty','Beauty'),
    ('Car Rental','Car Rental'),
	('Catering','Catering'),
    ('Cleaning','Cleaning'),
	('Computer & IT','Computer & IT'),
    ('Event Planning','Event Planning'),
	('Fitness','Fitness'),
    ('Interior Design','Interior Design'),
	('Logistics','Logistics'),
    ('Massage Therapy','Massage Therapy'),
	('Pet','Pet'),
    ('Photography & Video','Photography & Video'),
	('Real Estate','Real Estate'),
    ('Renovation','Renovation'),
	('Repair','Repair'),
    ('Travel Agencies','Travel Agencies'),
	('Web Design','Web Design'),
    ('Wedding','Wedding'),
	('Others','Others'),
   )
	Title = models.CharField(max_length=30,blank=False)
	category = models.CharField("Category", max_length=255, choices=MAYBECHOICE2,blank=True)
	company_name = models.CharField(max_length=50,blank=False)
	description = models.CharField(max_length=200,blank=True)
	attachment = models.FileField(upload_to='dashboard/',blank=False,null=False)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	location = models.CharField(max_length=255,blank=True)
	created_at = models.DateTimeField()
	email = models.EmailField(blank=True)
	cellphone = models.IntegerField(blank=True,default=1)
	payment_info = models.CharField(max_length=255,blank=False,default="Mpesa Paybill Number: 914226, Account Number:Name of Service Porvider")


	def __unicode__(self):
		return self.Title

class payment(models.Model):
	payment_id = models.CharField(max_length=255,blank=True)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=2)