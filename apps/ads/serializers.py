# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework.fields import IntegerField, CharField
from rest_framework.serializers import ModelSerializer

from apps.ads.models import Category, AdvertisementImage, District, Advert, Region, FavoriteAdvertisement
from apps.users.models import User


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "id", 'name', 'parent'

    def get_fields(self):
        fields = super(CategoryModelSerializer, self).get_fields()
        fields['children'] = CategoryModelSerializer(many=True, required=False)
        return fields


class AdvertisementModelSerializer(ModelSerializer):
    class Meta:
        model = Advert
        fields = 'id', 'name', 'price', 'created_at', 'city'
        read_only_fields = 'slug',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['image'] = AdvertisementImageSerializer(instance.advert.images.all(), many=True).data
        return repr


class DistrictModelSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = 'id', 'name',


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = 'id', 'name', 'district',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['district'] = DistrictModelSerializer(instance.district).data
        return repr


class AdvertisementImageSerializer(ModelSerializer):
    class Meta:
        model = AdvertisementImage
        fields = 'id', 'image'


class FavoriteAdsModelSerializer(ModelSerializer):
    product_id = IntegerField()

    class Meta:
        model = FavoriteAdvertisement
        fields = '__all__'

    def save(self, *, raise_exception=False):
        advert = self.initial_data['advert']
        user = self.initial_data['user']
        favorite_obj, create_obj = FavoriteAdvertisement.objects.get_or_create(user_id=user, advert_id=advert)
        if not create_obj:
            favorite_obj.delete()

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['product_image'] = AdvertisementImageSerializer(instance.advert.images.all(), many=True).data
        product_data = AdvertisementModelSerializer(instance.product).data
        filtered_product_data = {
            'id': product_data['id'],
            'name': product_data['name'],
            'price': product_data['price'],
            'city': f"{instance.product.city.region.name}, {instance.product.city.name}",
            'created_at': product_data['created_at']
        }
        repr['product_data']: filtered_product_data
        return repr


class ChangeUserPasswordModelSerializer(ModelSerializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)
    '''
    to check validation of new password add validators=[validate_password]
    '''

    class Meta:
        model = User
        fields = "old_password", 'new_password',

    # def validate_new_password(self, value):
    #     if len(value) < 8:
    #         raise ValidationError('Invalid password, enter more than 8 chars')
    #     if value.isalnum():
    #         raise ValidationError('password must have at least one special character.')
    #     return value


class AdvertSerializer(ModelSerializer):
    class Meta:
        model = Advert
        fields = ['name', 'description']
