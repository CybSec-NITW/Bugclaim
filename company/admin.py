from django.contrib import admin

# Register your models here.
from company.models import CompanyAdmin, CompanyMod

admin.site.register(CompanyAdmin)
admin.site.register(CompanyMod)