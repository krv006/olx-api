from django.urls import path, include

urlpatterns = [
    path('ads/', include('ads.urls')),
    path('users/', include('users.urls')),
]
