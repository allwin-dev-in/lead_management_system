from django.urls import path

from leads.views import LeadsCreateView
from leads.views import LeadsListView
from leads.views import LeadRetriveUpdateDelete

urlpatterns=[
    path("create/",LeadsCreateView.as_view()),
    path("all/",LeadsListView.as_view()),
    path("<int:pk>/",LeadRetriveUpdateDelete.as_view()),
    
]