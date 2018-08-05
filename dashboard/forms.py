from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from dashboard.models import services,Inquiries,payment

class ServiceForm(forms.ModelForm):
	Title = forms.CharField(label='Service Name:',max_length=200,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	company_name = forms.CharField(label='Company Name:',max_length=200,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	cellphone=forms.IntegerField(label="Cellphone:",required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(label="Your email:", required = True,max_length=70,widget=forms.TextInput(attrs={'multiple':True,'class':'form-control','name':'email'}))
	attachment = forms.FileField(label="Images:",required=True,widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple':"true",'name':'attachment'}))
	location = forms.CharField(label="Location:", required =True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control','name':'location'}))
	description = forms.CharField(label="Description:", required=True,max_length=250,widget=forms.Textarea(attrs={'class':'form-control','name':'description','rows':'6'}))
	payment_info = forms.CharField(label="Payment Information", required =True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control','name':'payment_info'}))


	class Meta:
		model = services
		fields = ('Title','company_name','attachment','email','location','cellphone','payment_info','description')

	def clean_cellphone(self):
		cellphone = self.cleaned_data.get("cellphone")
		if cellphone=="":
			raise forms.ValidationError("Please enter a valid phone number!")
		return cellphone

	def save(self, commit=True):
		services = super(ServicesForm,self).save(commit=False)
		if commit:
			services.save()
		return services

class DateInput(forms.DateTimeInput):
	input_type = 'date'

class TimeInput(forms.DateTimeInput):
	input_type = 'time'

class InquiriesForm(forms.ModelForm):
	client_name = forms.CharField(label='Your Name:',max_length=200,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	cellphone=forms.CharField(label="Cellphone:",required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	client_email = forms.CharField(label="Your email:", required = True,max_length=70,widget=forms.TextInput(attrs={'multiple':True,'class':'form-control','name':'email'}))
	message = forms.CharField(label="Your message?:", required=True,max_length=250,widget=forms.Textarea(attrs={'class':'form-control','name':'message','rows':'6'}))
	transaction_code = forms.CharField(label="Transaction code:",help_text="Pay the fee to paybill number 914226 ,then enter the transaction code you received here." ,required =True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control','name':'Transaction_code'}))
	booked_time = forms.DateTimeField(label='Schedule a date:',required=True,widget=DateInput(attrs={'class':'form-control'}))
	
	class Meta:
		model = Inquiries
		fields = ('client_name','client_email','cellphone','booked_time','transaction_code','message')

	def clean(self,*args,**kwargs):
		trans = self.cleaned_data.get("transaction_code")
		if not payment.objects.all().filter(payment_id__iexact=trans):
			raise forms.ValidationError("Sorry ,the transaction code you provided is invalid!")
		return super(InquiriesForm,self).clean(*args,**kwargs)


	def clean_cellphone(self):
		cellphone = self.cleaned_data.get("cellphone")
		if cellphone=="":
			raise forms.ValidationError("Please enter a valid phone number!")
		return cellphone

	def save(self, commit=True):
		Inquiries = super(InquiriesForm,self).save(commit=False)
		if commit:
			Inquiries.save()
		return Inquiries