from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from jsonschema._format import is_email
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.users.serializers import UserModelSerializer, UserLoginSerializer


@extend_schema(tags=['user'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

# @extend_schema(tags=['user'])
# class LoginAPIView(GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserLoginSerializer
#     permission_classes = AllowAny,
#
#     def post(self, request):
#         if not is_email(request.data['email_or_phone_number']):
#             user = authenticate(request=request, username=request.data['email_or_phone_number'],
#                                 password=request.data['password'])
#             refresh = RefreshToken.for_user(user)
#             return Response({"access": str(refresh.access_token), "refresh": str(refresh)})
#         # else:
#         #     user = User.objects.filter(phone_number=request.data['email_or_phone_number'], password=request.data['password'])
#         # return user
