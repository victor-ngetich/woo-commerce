from __future__ import absolute_import ,unicode_literals
from dashboard.models import Inquiries,services
import django_tables2 as tables


class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name

class InquiriesTable(tables.Table):
	amend = CheckBoxColumnWithName(verbose_name="Select", accessor="pk")
	class Meta:
		model = Inquiries
		fields = ('client_name','client_email','created_at','order_number','cellphone','booked_time','payment_status','transaction_code','message','amend')

class servicesTable(tables.Table):
	amend = CheckBoxColumnWithName(verbose_name="Select", accessor="pk")
	class Meta:
		model = services
		fields = ('Title','company_name','email','cellphone','attachment','user_id','created_at','location','payment_info','description','amend')
