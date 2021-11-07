from django.contrib import admin
from .models import *

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User info',  {'fields': ['first_name', 'last_name', 'email', 'tax_no']}),
        ('Additional', {'fields': ['gender', 'role']}) # itd
    ]
    
    list_display = ('first_name', 'last_name', 'email', 'tax_no')

    search_fields = ['first_name']


class AddressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Adress info',  {'fields': ['street', 'house_no', 'city']})
    ]

    list_display = ('street', 'house_no', 'city')

    search_fields = ['street']


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company info',  {'fields': ['tax_no', 'name', 'address', 'ceo']})
    ]

    list_display = ('tax_no', 'name', 'address', 'ceo')

    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('City info',  {'fields': ['post_no', 'name']})
    ]

    list_display = ('post_no', 'name')

    search_fields = ['name']


class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Role info',  {'fields': ['name', 'min_hourly_rate']})
    ]

    list_display = ('name', 'min_hourly_rate')

    search_fields = ['name']


# ovo ne moze ovako...
class WorkhourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Role info',  {'fields': ['staff_id', 'comp_id', 'date_from', 'date_until']})
    ]

    list_display = ('staff_id', 'comp_id', 'date_from', 'date_until')

    search_fields = ['staff_id']



admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Workhour, WorkhourAdmin)