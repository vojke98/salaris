from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Company)
admin.site.register(User_Company)
admin.site.register(Workhour)