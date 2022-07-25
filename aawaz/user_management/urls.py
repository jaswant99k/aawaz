from django.urls import path
from .views import ProfileUpdateAPIView, SocialLoginView, UserDetailAPI,RegisterUserAPIView
urlpatterns = [
  path("get-details/",UserDetailAPI.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  path('profile-update/', ProfileUpdateAPIView.as_view()),
  path('oauth/login/', SocialLoginView.as_view()),
]