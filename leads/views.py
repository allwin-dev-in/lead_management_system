from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from leads.serializers import LeadSerializer
from leads.models import LeadModel
from leads.permissions import IsOwner

# Create your views here.


class LeadsCreateView(CreateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    serializer_class=LeadSerializer

class LeadsListView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=LeadModel.objects.filter(created_by=request.user)
        serializer_instance=LeadSerializer(qs,many=-True)
        return Response(serializer_instance.data)

class LeadRetriveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsOwner]

    serializer_class=LeadSerializer
    queryset=LeadModel.objects.all()


