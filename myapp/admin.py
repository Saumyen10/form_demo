from django.contrib import admin
from myapp.models import Zone, Division, SubDivision , Consumer
# Register your models here.

admin.site.register(Zone)
admin.site.register(Division)
admin.site.register(SubDivision)
admin.site.register(Consumer)