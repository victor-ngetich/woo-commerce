from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from dashboard.tables import InquiriesTable,servicesTable
from dashboard.models import Inquiries,services
from django_tables2 import RequestConfig
# Create your views here.
def home(request):
	displays = services.objects.all()
	banner = services.objects.latest('created_at')
	return render(request, 'home/app.html',{'displays':displays,'banner':banner})

def categorized(request):
	a = request.GET.get('cat', None)
	print(a)
	displays = services.objects.all().filter(category__icontains=a)
	banner = services.objects.latest('created_at')
	return render(request, 'home/app2.html',{'displays':displays,'banner':banner})

def serv(request):
	return render(request, 'home/app3.html')

def about(request):
	return render(request, 'home/app4.html')

def search(request):
	if request.method=="POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''


	articles =  services.objects.all().filter(Title__icontains=search_text)[:5]

	return render(request,'home/ajax_search.html',{'articles':articles})