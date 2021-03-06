from .serializers import UserSerializer
from rest_framework import viewsets, routers, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User
from psql_users.settings import SIGN_API
import hashlib

"""
class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = User.objects.all()
        print("ass - -as ", (self.request.query_params.get('apikey')))
        sign = "%s-%s-%s" % (self.request.user.username, SIGN_API, self.request.user.password)

        return queryset
"""

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def users(request):
    apikey = request.META.get("HTTP_APIKEY")
    username = request.user.username
    email = request.user.email
    sign = "%s-%s-%s" % (username, SIGN_API, email)
    apikey_user = "trafilea" + hashlib.md5(sign.encode('utf-8')).hexdigest()

    if apikey != apikey_user:
        return Response({"status" : "APIKeyinvalid"}, status=401)

    users = UserSerializer(User.objects.all(), many=True).data
    return Response(users)
