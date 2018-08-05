from dashboard.models import services,Inquiries
from dashboard import views
from django.conf.urls import url,include
from django.views.generic import ListView,DetailView

urlpatterns = [
url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Inquiries,template_name = 'dashboard/inquiries.html')),
url(r'^$',views.bookings,name = 'bookings'),
]