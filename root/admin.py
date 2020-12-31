from django.contrib import admin

# Register your models here.
from root.models import RootAdmin, Rootmod

admin.site.register(RootAdmin)
admin.site.register(Rootmod)