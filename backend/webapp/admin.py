from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User info',  {'fields': ['first_name', 'last_name', 'address', 'email', 'tax_no', 'company', 'role']})
    ]

    list_display = ('first_name', 'last_name', 'address', 'email', 'tax_no', 'address', 'company', 'role')

    search_fields = ['first_name']


class AddressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Adress info',  {'fields': ['street', 'house_no', 'city']})
    ]

    list_display = ('street', 'house_no', 'city')

    search_fields = ['street']


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company info',  {'fields': ['tax_no', 'name', 'address']})
    ]

    list_display = ('tax_no', 'name', 'address')

    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('City info',  {'fields': ['post_no', 'name']})
    ]

    list_display = ('post_no', 'name')

    search_fields = ['name']


class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Role info',  {'fields': ['company', 'name', 'min_hourly_rate', 'is_admin']})
    ]

    list_display = ('company', 'name', 'min_hourly_rate', 'is_admin')

    search_fields = ['name']



class WorkhourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Workhours info',  {'fields': ['user', 'company', 'date_from', 'date_until', 'hourly_rate_at_the_time']})
    ]

    list_display = ('user', 'company','date_from', 'date_until', 'hourly_rate_at_the_time')

    search_fields = ['user']


class JoinRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Join Requests info',  {'fields': ['user', 'company', 'request_date']})
    ]

    list_display = ('user', 'company', 'request_date')

    search_fields = ['user']


class LeaveRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Leave Requests info',  {'fields': ['user', 'company', 'request_date']})
    ]

    list_display = ('user', 'company', 'request_date')

    search_fields = ['user']




admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Workhour, WorkhourAdmin)
admin.site.register(JoinRequest, JoinRequestAdmin)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
