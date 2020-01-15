"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from accounts.views import (login_view, register_view,logout_page,reset_view,refer_view,success)
from dashboard.views import (dashboard,post,inventory,bookings,delete,search)
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite import admin_auth
from accounts.views import (login_view, register_view, success)
from home.views import (home, serv, about, categorized, search)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('django.contrib.auth.urls')),  
    url(r'^',include('home.urls')),
    url(r'^accounts/login/',login_view,name='login'),
    # url(r'^$', login_view, name='login_view'),
    url(r'^home', home, name='index'),
    url(r'^catt/',categorized,name='categorized'),
    url(r'^about/',about,name='about'),
    url(r'^serv/',serv,name='serv'),   
    url(r'^accounts/logout/',logout_page,name='logout'),
    url(r'^register/',register_view,name='register'),
    url(r'^reset/',reset_view,name='reset'),
    url(r'^refer/',refer_view,name='refer'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',include('accounts.urls')),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  
    url(r'^dashboard/',dashboard,name='dashboard'),
    url(r'^success/',success,name='success'),
    url(r'^post/',post,name='post'),
    url(r'^inventory/',inventory,name='inventory'),
    url(r'^bookings/',include('dashboard.urls')),
    url(r'^search/',search,name='search'),
    url(r'^delete/',delete,name='delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
