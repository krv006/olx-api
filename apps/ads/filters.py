from django_filters import BooleanFilter, ModelChoiceFilter
from django_filters.rest_framework import FilterSet, CharFilter

from apps.ads.models import Advert, Region, District


class AdsFilterSet(FilterSet):
    output_image = BooleanFilter(method='get_output_image')
    max_price = CharFilter(method='get_max_price')
    min_price = CharFilter(method='get_min_price')

    class Meta:
        model = Advert
        fields = 'category', 'currency', 'output_image', 'max_price', 'min_price'

    def get_max_price(self, queryset, name, value):
        return queryset.filter(price__lte=value)

    def get_min_price(self, queryset, name, value):
        return queryset.filter(price__gte=value)

    def get_output_image(self, queryset, name, value):
        value = False if value else True
        return queryset.filter(images__isnull=value)


class RegionFilter(FilterSet):
    district = ModelChoiceFilter(queryset=District.objects.all(), method='filter_by_district')

    class Meta:
        model = Region
        fields = '__all__'

    def filter_by_district(self, queryset, name, value):
        return queryset.filter(district=value)
