from django.contrib import admin
from .models import Login,rtouser,Learners,licence,Vehi_Reg,NOC,Ownership_transfer,Test_date,Payment,Hazmate,PSV_Badge,International_dl,Adhaar

# Register your models here.
admin.site.register(Login),
admin.site.register(rtouser),
admin.site.register(Learners),
admin.site.register(licence),
admin.site.register(Vehi_Reg),
admin.site.register(NOC),
admin.site.register(Ownership_transfer),
admin.site.register(Test_date),
admin.site.register(Payment),
admin.site.register(Hazmate),
admin.site.register(PSV_Badge),
admin.site.register(International_dl),
admin.site.register(Adhaar)


