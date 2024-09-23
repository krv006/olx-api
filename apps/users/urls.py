from django.urls import path
from apps.users.views import UserListAPIView, LoginAPIView

urlpatterns = [
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('user/login/', LoginAPIView.as_view(), name='login-page'),
]
