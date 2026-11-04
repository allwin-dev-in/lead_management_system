from django.urls import path

from leads.views import LeadsCreateView

urlpatterns=[
    path("create/",LeadsCreateView.as_view()),
    
]