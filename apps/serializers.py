from rest_framework.serializers import ModelSerializer

from apps.models import Product


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'name',
