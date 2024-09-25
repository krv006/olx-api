from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.ads.models import AdvertisementImage, Advert, FavoriteAdvertisement, Region, District, Category, ExtraFields, \
    Message, Currency, WorkAds, ProductHistory
from apps.users.models import User


# Register your models here.
@admin.register(AdvertisementImage)
class AdvertisementImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkAds)
class WorkAdsAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductHistory)
class ProductHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteAdvertisement)
class FavoriteAdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(ExtraFields)
class ExtraFieldsAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Advert)
class AdvertImageAdmin(admin.ModelAdmin):
    pass

