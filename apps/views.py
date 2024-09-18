from rest_framework.generics import ListCreateAPIView

from apps.models import Product
from apps.serializers import ProductModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
