from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from dashboard.tables import InquiriesTable,servicesTable
from dashboard.models import Inquiries,services
from django_tables2 import RequestConfig
import datetime
from django.contrib import messages
from django.utils import timezone
from dashboard.forms import ServiceForm,InquiriesForm
from django.contrib import messages
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
	)
# Create your views here.


@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Merchant').exists())
def dashboard(request):
	now = datetime.datetime.now()
	# inq= len(Inquiries.objects.all().filter(user_id = request.user))
	# inv = len(services.objects.all().filter(user_id = request.user))
	inquiries = InquiriesTable(Inquiries.objects.all().order_by('-created_at'))
	RequestConfig(request, paginate={"per_page": 5}).configure(inquiries)

	return render(request, 'dashboard/index.html',{'now':now,'inquiries':inquiries})
@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Merchant').exists())
def post(request):
	if request.method=="POST":
		form = ServiceForm(request.POST , request.FILES)

		if form.is_valid():
			title = form.cleaned_data['Title']
			category = form.cleaned_data['category']
			company = form.cleaned_data['company_name']
			cell = form.cleaned_data['cellphone']
			email = form.cleaned_data['email']
			location = form.cleaned_data['location']
			description = form.cleaned_data['description']
			pay = form.cleaned_data['payment_info']

			for f in request.FILES.getlist("attachment"):
				services.objects.create(attachment=f,Title=title, category=category, email=email,company_name=company,cellphone=cell,location=location,payment_info=pay,description=description,user_id=request.user,created_at=timezone.now())
			return HttpResponseRedirect('/inventory/')
			messages.info(request, 'Your product was posted successfully.')
		else:
			return render(request, 'dashboard/post.html',{"form":form})
	else:			
		form = ServiceForm()
		args = {'form':form}
		args.update(csrf(request))
		args['form'] = ServiceForm()
		return render(request, 'dashboard/post.html',args)

@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Merchant').exists())
def inventory(request):
	now = datetime.datetime.now()
	inventory = servicesTable(services.objects.all().filter(user_id = request.user).order_by('-created_at'))
	RequestConfig(request, paginate={"per_page": 5}).configure(inventory)

	return render(request, 'dashboard/inventory.html',{'now':now,'inventory':inventory})

def bookings(request):
	if request.method=="POST":
		form = InquiriesForm(request.POST or None)

		if form.is_valid():
			name = form.cleaned_data['client_name']
			email = form.cleaned_data['client_email']
			cell = form.cleaned_data['cellphone']
			message = form.cleaned_data['message']
			trans= form.cleaned_data['transaction_code']
			d = form.cleaned_data['booked_time']
			
			Inquiries.objects.create(client_name=name,client_email=email,cellphone=cell,transaction_code=trans,message=message,booked_time=d,created_at=timezone.now())
			messages.info(request, 'Thank you for submitting your inquiry,we will get back to you shortly.')
			return HttpResponseRedirect('/')
		else:
			return render(request, 'dashboard/inquiries.html',{"form":form})
	else:			
		form = InquiriesForm()
		args = {'form':form}
		args.update(csrf(request))
		args['form'] = InquiriesForm()
		return render(request, 'dashboard/inquiries.html',args)
@csrf_protect
@ensure_csrf_cookie
@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Merchant').exists())
def delete(request):
	if request.method == 'POST':
		inquiry = Inquiries.objects.all()
		item_id = len(request.POST.get('item_id'))  
		item = Inquiries.objects.get(order_number=item_id)
		item.delete()
		return render_to_response('dashboard/index.html', {'form':form, 'inquiry':inquiry}, RequestContext(request))

def search(request):
	pass