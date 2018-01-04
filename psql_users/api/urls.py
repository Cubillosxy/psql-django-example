from django.urls import path, include
from rest_framework import routers
from .viewsets import  users

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet, base_name="users")

urlpatterns = [
    #path('', include(router.urls)),
    path('users/', users, name="users")
]