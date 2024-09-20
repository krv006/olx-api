from django.urls import path, include

urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.ads.urls')),
]
