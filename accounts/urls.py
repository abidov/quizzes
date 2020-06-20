from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', views.ProfileView.as_view(), name='account-profile'),
]
