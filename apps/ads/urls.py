from django.urls import path

from apps.users.views import UserListAPIView

urlpatterns = [
    path('user/', UserListAPIView.as_view(), name='user-list'),
    # path('test-login/', LoginAPIView.as_view()),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('change-password/', ChangePasswordUserGenericAPIView.as_view()),
    # path('login/', UserListAPIView.as_view()),
]