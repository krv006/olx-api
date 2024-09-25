from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.ads.views import CategoryListAPIView, AdvertisementListAPIView, DistrictListAPIView, \
    FavoriteAdsListCreateAPIView, \
    ChangePasswordUpdateAPIView, AdvertViewSet, RegionListCreateView

router = DefaultRouter()

router.register('adverts', AdvertViewSet, 'adverts')
urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view()),
    path('ads/', AdvertisementListAPIView.as_view(), name='avert-list'),
    path('district/', DistrictListAPIView.as_view()),
    path('region/', RegionListCreateView.as_view()),
    path('fav-ads/', FavoriteAdsListCreateAPIView.as_view()),
    path('change-password/', ChangePasswordUpdateAPIView.as_view()),

]
