from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', views.ProfileView.as_view(), name='account-profile'),
    path('profile/test/', views.profile_test_result, name='profile-test-result'),
    path('profile/test/<int:test_id>/<int:test_result_id>/',
         views.profile_test_result_detail,
         name='profile-test-result-detail'),
]
