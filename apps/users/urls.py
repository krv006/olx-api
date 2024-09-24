from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import UserListCreateAPIView, LoginAPIView

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view(), name='user-list'),
    path('test-login/', LoginAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
