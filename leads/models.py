from django.db import models

from accounts.models import User
# Create your models here.

class LeadModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12,unique=True)
    company=models.CharField(max_length=200,null=True)
    SOURCE_CHOICES=(
        ("Website","Website"),
        ("Social Media","Social Media"),
        ("Referral","Referral"),
        ("Advertisement","Advertisement"),
        ("Other","Other")
    )
    source=models.CharField(max_length=100,choices=SOURCE_CHOICES,default="Website")
    STATUS_CHOICES=(
        ("New","New"),
        ("Contacted","Contacted"),
        ("Interested","Interested"),
        ("Converted","Converted"),
        ("Lost","Lost")
    )
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default="New")
    description=models.TextField(null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="leads")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)