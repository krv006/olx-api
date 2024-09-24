
from django_elasticsearch_dsl_drf.filter_backends import SuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.ads.document import AdvertDocument
from apps.ads.filters import AdsFilterSet
from apps.ads.models import Category, Advert, District, FavoriteAdvertisement
from apps.ads.pagination import LargeResultsSetPagination
from apps.ads.serializers import CategoryModelSerializer, AdvertisementModelSerializer, DistrictModelSerializer, \
    FavoriteAdsModelSerializer, ChangeUserPasswordModelSerializer, AdvertDocumentSerializer
from apps.users.models import User


@extend_schema(tags=['category'])
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.filter(level=0)
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['ad'])
class AdvertisementListAPIView(ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertisementModelSerializer
    filter_backends = OrderingFilter, DjangoFilterBackend
    filterset_class = AdsFilterSet
    # filterset_fields = 'image__id',
    ordering_fields = ['price', 'created_at']
    search_fields = 'name', 'description'
    pagination_class = LargeResultsSetPagination


@extend_schema(tags=['district'])
class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictModelSerializer
    filter_backends = DjangoFilterBackend, SearchFilter
    search_fields = 'name', 'region__name'


@extend_schema(tags=['favorite_ads'])
class FavoriteAdsListCreateAPIView(ListCreateAPIView):
    queryset = FavoriteAdvertisement.objects.all()
    serializer_class = FavoriteAdsModelSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@extend_schema(tags=['change_password'])
class ChangePasswordUpdateAPIView(UpdateAPIView):
    serializer_class = ChangeUserPasswordModelSerializer
    model = User

    permission_classes = IsAuthenticated,

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
pbkdf2_sha256$870000$bNKoEN3Rptr5gJ9GADttad$PyhtirAJjfN2NQFA7/W3XJTr4S2DLbmV0aBBABLjelA=
pbkdf2_sha256$870000$7N6kpXrfQXjkf7BpQfUxcd$/rd76oQfkhEEDf0rYiux8sTlaAQvB7b17KhnkC+QRzk=
'''


class AdvertDocumentView(DocumentViewSet):
    document = AdvertDocument
    serializer_class = AdvertDocumentSerializer
    filter_backends = SearchFilter, SuggesterFilterBackend
    search_fields = 'name', 'description'
