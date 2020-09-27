from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from NGO_App.serializers import UserProfileSerializer,NgoProfileSerializer,NgoRequirementsSerializer,RecieptSerializer,LoginSerializer
from NGO_App.models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import permissions,viewsets,generics
from rest_framework.views import APIView,status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token


class UserProfileView(generics.ListCreateAPIView):
     queryset = UserProfile.objects.all()
     serializer_class =UserProfileSerializer

class NgoProfileView(generics.ListCreateAPIView):
     queryset = NGOProfile.objects.all()
     serializer_class =NgoProfileSerializer


class NgoRequirementsView(generics.ListCreateAPIView):
     queryset = NgoRequirements.objects.all()
     serializer_class =NgoRequirementsSerializer

class RecieptView(generics.ListCreateAPIView):
     queryset = Reciept.objects.all()
     serializer_class =RecieptSerializer

class NgoLogin(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):

        email = request.data.get("email")
        password = request.data.get("password")
        print(email,password)

        #print(serializer.email)
        user = authenticate(username=email,password=password)
        print(user)
        if user is not None:
            #token=Token.objects.get(user=user)


            login(request, user)


            data = {
                "Name": NGOProfile.objects.get(user=user).ngo_name,
                "id": user.pk,
                "Username": user.username,
                "Message":"done",
                


            }


            return Response(data)

        else:
            data = {"Message": "There was error authenticating"}
            return JsonResponse(data)


class UserLogin(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):

        email = request.data.get("email")
        password = request.data.get("password")
        print(email,password)
        #print(serializer.email)
        user = authenticate(username=email,password=password)

        if user is not None:
            #token=Token.objects.get(user=user)


            login(request, user)






            data = {
                "Name": UserProfile.objects.get(user=user).user.first_name+" "+UserProfile.objects.get(user=user).user.last_name,
                "id": user.pk,
                "Username": user.username,
                "Message":"done",



            }


            return Response(data)

        else:
            data = {"Message": "There was error authenticating"}
            return JsonResponse(data)
