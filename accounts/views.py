from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import User
from accounts.serializers import UserSerializer

# Create your views here.

class SignupView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            qs=User.objects.create_user(**cleaned_data)
            ser_inst=UserSerializer(qs)
            return Response(ser_inst.data)
        else:
            return Response(serializer_instance.errors)

class ProfileDetailView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        print(request.user)
        ser_inst=UserSerializer(request.user)
        return Response(data=ser_inst.data)
