from __future__ import unicode_literals
from django.contrib import admin
from dashboard.models import Inquiries,services
 
class EventModelAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_email", "cellphone", "order_number", 'created_at','user_id','message']
    list_display_links = ["client_name"]
    list_filter = ["client_name","client_email","order_number","created_at","user_id"]
    list_per_page = 10
    list_editable = []
    search_fields = ["client_name","client_email", "cellphone", "order_number", 'created_at']

    class Meta:
        model = Inquiries

class EventModelAdmin1(admin.ModelAdmin):
    list_display = ["Title", "company_name","email","user_id","cellphone","attachment",'created_at',"description"]
    list_display_links = ["Title"]
    list_filter = ["Title","email","user_id","cellphone","created_at"]
    list_per_page = 5
    list_editable = []
    search_fields = ["Title","company_name","email","cellphone", "created_at"]

    class Meta:
        model = services

admin.site.register(Inquiries,EventModelAdmin)
admin.site.register(services,EventModelAdmin1)