from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from polymorphic.models import PolymorphicModel
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
	payment_status = models.BooleanField(max_length=3, choices=MAYBECHOICE,default=1)
	booked_time = models.DateField(blank=False,default="2018-07-20")
	def __unicode__(self):
		return self.Client_name


class services(models.Model):
	Title = models.CharField(max_length=30,blank=False)
	company_name = models.CharField(max_length=50,blank=False)
	description = models.CharField(max_length=200,blank=True)
	attachment = models.FileField(upload_to='dashboard/',blank=False,null=False)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	location = models.CharField(max_length=255,blank=True)
	created_at = models.DateTimeField()
	email = models.EmailField(blank=True)
	cellphone = models.IntegerField(blank=True,default=1)
	payment_info = models.CharField(max_length=255,blank=False,default="Mpesa paybill number-914226")


	def __unicode__(self):
		return self.Title

class payment(models.Model):
	payment_id = models.CharField(max_length=255,blank=True)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=2)