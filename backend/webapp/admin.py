from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User info',  {'fields': ['first_name', 'last_name', 'address', 'email', 'tax_no', 'company', 'role', 'qualifications', 'user_about_info']})
    ]

    list_display = ('pk', 'first_name', 'last_name', 'address', 'email', 'tax_no', 'company', 'role', 'qualifications', 'user_about_info')

    search_fields = ['first_name', 'last_name', 'address__street', 'address__house_no', 'address__city__post_no', 'address__city__name', 'email', 'tax_no', 'company__tax_no', 'company__name', 'role__name']


class AddressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Adress info',  {'fields': ['street', 'house_no', 'city']})
    ]

    list_display = ('pk', 'street', 'house_no', 'city')

    search_fields = ['street', 'house_no', 'city__post_no', 'city__name']


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company info',  {'fields': ['reference_key', 'tax_no', 'name', 'address', 'company_about_info']})
    ]

    list_display = ('pk', 'reference_key', 'tax_no', 'name', 'address', 'company_about_info')

    search_fields = ['tax_no', 'name', 'address__street', 'house_no', 'address__city__post_no', 'address__city__name']


class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('City info',  {'fields': ['post_no', 'name']})
    ]

    list_display = ('post_no', 'name')

    search_fields = ['post_no', 'name']


class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Role info',  {'fields': ['company', 'name', 'min_hourly_rate', 'is_admin']})
    ]

    list_display = ('pk', 'company', 'name', 'min_hourly_rate', 'is_admin')

    search_fields = ['name', 'min_hourly_rate', 'is_admin', 'company__name', 'company__address__street', 'company__address__house_no', 'company__address__city__post_no', 'company__address__city__name']



class WorkhourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Workhours info',  {'fields': ['user', 'company', 'date_from', 'date_until', 'hourly_rate_at_the_time']})
    ]

    list_display = ('pk', 'user', 'company', 'date_from', 'date_until', 'hourly_rate_at_the_time')

    search_fields = ['user__first_name', 'user__last_name', 'user__address__street', 'user__address__house_no', 'user__address__city__post_no', 'user__address__city__name', 'user__email', 'user__tax_no', 'company__tax_no', 'company__name', 'user__role__name', 'date_from', 'date_until', 'hourly_rate_at_the_time']


class JoinRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Join Requests info',  {'fields': ['user', 'company', 'request_date', 'response_date', 'status']})
    ]

    list_display = ('pk', 'user', 'company', 'request_date', 'response_date', 'status')

    search_fields = ['user__first_name', 'user__last_name', 'user__address__street', 'user__address__house_no', 'user__address__city__post_no', 'user__address__city__name', 'user__email', 'user__tax_no', 'company__tax_no', 'company__name', 'user__role__name', 'request_date', 'response_date', 'status']


admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Workhour, WorkhourAdmin)
admin.site.register(JoinRequest, JoinRequestAdmin)
