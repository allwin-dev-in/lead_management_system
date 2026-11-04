from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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
    def get(self,request):
        qs=User.objects.filter(username=request.user)
        ser_inst=UserSerializer(qs,many=True)
        return Response(data=ser_inst.data)
