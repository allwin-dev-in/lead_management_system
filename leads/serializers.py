from rest_framework import serializers

from leads.models import LeadModel

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeadModel
        fields="__all__"
        read_only_fields=["id","created_by","created_at","updated_at"]
