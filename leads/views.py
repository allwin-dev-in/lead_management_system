from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.generics import CreateAPIView,ListAPIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from leads.serializers import LeadSerializer
from leads.models import LeadModel

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


