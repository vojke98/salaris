from django.db.models import fields
from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):

    post_no = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=50, required=True)

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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"



class WorkhourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workhour
        fields = "__all__"


class JoinRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = JoinRequest
        fields = "__all__"
