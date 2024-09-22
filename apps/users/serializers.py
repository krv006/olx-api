from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(Serializer):
    email_or_phone_number = CharField(required=True)
    password = CharField(required=True)

    def validate(self, attrs):
        return super().validate(attrs)


class ChangePasswordUserModelSerializer(ModelSerializer):
    user = CharField()
    new_password = CharField(required=True)
    old_password = CharField(required=True)

    class Meta:
        model = User
        fields = 'new_password', 'old_password', 'user'
