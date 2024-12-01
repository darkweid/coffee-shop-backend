from django.urls import path
from .views import (UserRegistrationView, UserDetailView, UserVerificationView,
                    UserAuthenticationView, UserListView, MeView)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('me/', MeView.as_view(), name='me'),
    path('verification/', UserVerificationView.as_view(), name='user-verification'),
    path('authentication/', UserAuthenticationView.as_view(), name='authentication'),
    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

]
