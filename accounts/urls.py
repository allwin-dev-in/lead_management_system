from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import SignupView
from accounts.views import ProfileDetailView




urlpatterns=[
    path("register/",SignupView.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("profile/",ProfileDetailView.as_view()),
    
]