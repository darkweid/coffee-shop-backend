from django.urls import path
from .views import UserRegistrationView, UserDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
