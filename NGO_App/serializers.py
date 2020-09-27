from rest_framework import serializers
from NGO_App.models import *
from django.contrib.auth.models import User



class UserProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = UserProfile
        fields = ['id', 'address_line_1','contact','country','user']

class NgoProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = NGOProfile
        fields = ['id', 'address_line_1','contact','country','user','certificate','description','image']

class NgoRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NgoRequirements
        fields = ['id', 'ngo','requirement','quantity','message',]

class RecieptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciept
        fields = ['id', 'user','ngo_add_requirement','donated_items',]

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=10)
    password = serializers.CharField(style={"input_type": "password"})
