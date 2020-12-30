from django.contrib import admin
from .models import User,CompanyAdmin,CompanyMod,RootAdmin,Rootmod,Researcher
# Register your models here.

admin.site.register(User)
admin.site.register(CompanyAdmin)
admin.site.register(CompanyMod)
admin.site.register(RootAdmin)
admin.site.register(Rootmod)
admin.site.register(Researcher)