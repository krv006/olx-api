# from django.db.models import ImageField, CASCADE, BooleanField, TextField, JSONField, OneToOneField, IntegerField, \
#     CharField, DateTimeField, ForeignKey, Model, TextChoices
# from django_ckeditor_5.fields import CKEditor5Field
# from mptt.fields import TreeForeignKey
# from mptt.models import MPTTModel
#
# # from shared.django.models import BaseSlugModel
#
# from django.db.models import Model, CharField, SlugField
# from django.utils.text import slugify
#
#
# class BaseSlugModel(Model):
#     name = CharField(max_length=255)
#     slug = SlugField(max_length=255, unique=True)
#
#     def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
#         self.slug = slugify(self.name)
#         super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
#                      update_fields=update_fields)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.slug
#
#
# class Region(Model):
#     name = CharField(max_length=50)
#
#
# class District(Model):
#     name = CharField(max_length=50)
#     region = ForeignKey('ads.Region', CASCADE)
#
#
# class Category(BaseSlugModel, MPTTModel):
#     image = ImageField(upload_to='category/', null=True, blank=True)
#     parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')
#
#
# class ExtraFields(Model):
#     category = OneToOneField('ads.Category', CASCADE)
#     fields = JSONField(default=dict)
#
#
# class AdvertisementImage(Model):
#     advert = ForeignKey('ads.Advert', CASCADE, related_name='images')
#     image = ImageField(upload_to='product/')
#
#
# class FavoriteAdvertisement(Model):
#     advert = ForeignKey('ads.Advert', CASCADE, related_name='favorite')
#     user = ForeignKey('users.User', CASCADE, related_name='favorite')
#
#
# class Message(Model):
#     advert = ForeignKey('ads.Advert', CASCADE)
#     owner = ForeignKey('users.User', CASCADE)
#     text = TextField()
#
#
# class Currency(Model):
#     name = CharField(max_length=25)
#
#
# class Advert(BaseSlugModel):
#     class PaymentType(TextChoices):
#         CASH = 'cash', 'Cash'
#         FREE = 'free', 'Free'
#         EXCHANGE = 'exchange', 'Exchange'
#
#     class Status(TextChoices):
#         ACTIVE = 'active', 'Active'
#         WAITING = 'waiting', 'Waiting'
#         UNPAID = 'unpaid', 'Unpaid'
#         INACTIVE = 'inactive', 'Inactive'
#         REJECTED = 'rejected', 'Rejected'
#
#     status = CharField(max_length=20, choices=Status.choices, default=Status.WAITING)
#     category = ForeignKey('ads.Category', CASCADE)
#     price_type = CharField(max_length=10, choices=PaymentType.choices, default=PaymentType.CASH)
#     currency = ForeignKey('ads.Currency', CASCADE, null=True, blank=True)
#     price = IntegerField(null=True, blank=True)
#     description = TextField()
#     owner = ForeignKey('users.User', CASCADE)
#     city = ForeignKey('ads.District', CASCADE)
#     view_count = IntegerField(db_default=0)
#     is_new = BooleanField(default=False)
#     extra_filed_info = JSONField()
#
#     is_business = BooleanField(default=False)
#     contact = JSONField(default=dict)
#     updated_at = DateTimeField(auto_now_add=True)
#     created_at = DateTimeField(auto_now=True)
#     auto_renewal = BooleanField(db_default=False)
#
#
# class WorkAds(Model):
#     class WorkType(TextChoices):
#         PERMANENTLY = 'permanent', 'Permanent'
#         TEMPORARY = 'temporary', 'Temporary'
#
#     class TypeEmployment(TextChoices):
#         FULL_TIME = 'full time', 'Full time'
#         INCOMPLETE = 'incomplete', 'Incomplete'
#
#     min_price = IntegerField()
#     max_price = IntegerField()
#     category = ForeignKey('ads.Category', CASCADE)
#     contact = JSONField(default=dict)
#     description = CKEditor5Field()
#     title = CharField(max_length=255)
#     work_type = CharField(max_length=25, choices=WorkType.choices)
#     type_employment = CharField(max_length=25, choices=TypeEmployment.choices)
#     updated_at = DateTimeField(auto_now_add=True)
#     created_at = DateTimeField(auto_now=True)
#     owner = ForeignKey('users.User', CASCADE)
#     city = ForeignKey('ads.District', CASCADE)
#     auto_renewal = BooleanField(default=False)
#     extra_filed_info = JSONField()
#
#
# class ProductHistory(Model):
#     product_id = IntegerField()
#     product_name = CharField(max_length=255)
#     price = IntegerField()
#     deleted_at = DateTimeField(auto_now=True)


# from django.db.models import Model, CharField
#
#
# class Category(Model):
#     name = CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
