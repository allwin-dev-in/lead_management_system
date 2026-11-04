from rest_framework import serializers

from accounts.models import User

from leads.models import LeadModel
from leads.serializers import LeadSerializer

class UserSerializer(serializers.ModelSerializer):
    leads_details=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=["username","email","password","phone","leads_details"]

    def get_leads_details(self,obj):
        qs=LeadModel.objects.filter(created_by=obj)
        serializer_instance=LeadSerializer(qs,many=-True)
        return serializer_instance.data
