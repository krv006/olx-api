# from django_elasticsearch_dsl import Document
# from django_elasticsearch_dsl.registries import registry
#
# from apps.ads.models import Advert
#
#
# @registry.register_document
# class AdvertDocument(Document):
#     class Index:
#         name = "adverts"
#         settings = {
#             "number_of_shards": 1,
#             "number_of_replicas": 0,
#         }
#
#     class Django:
#         model = Advert
#         fields = [
#             "id",
#             "name",
#             "description"
#         ]
