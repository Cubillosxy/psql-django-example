from rest_framework import  serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    
    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username
        
    class Meta:
        model = User
        fields = ('username', 'email', 'created_at', 'last_login')
