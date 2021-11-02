from django.db.models import fields
from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        #fields = ("post_no", "name")
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class WorkhourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workhour
        fields = "__all__"
