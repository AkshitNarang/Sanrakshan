from django.contrib import admin
from .models import Admin_Details, Alerts, Emergency_Contacts, Department, News_and_Updates
from .models import Precautionary_Advisory, Schemes, Training_Data
# Register your models here.
# admin.site.register(AssingnedAuthority)
admin.site.register(Admin_Details)
admin.site.register(Alerts)
admin.site.register(Emergency_Contacts)
admin.site.register(Department)
admin.site.register(Precautionary_Advisory)
admin.site.register(News_and_Updates)
admin.site.register(Schemes)
admin.site.register(Training_Data)
# # PrecautionaryAdvisory
