from django.urls import path

from apps.views import ProductListCreateAPIView

urlpatterns = [
    path('product/', ProductListCreateAPIView.as_view()),
]