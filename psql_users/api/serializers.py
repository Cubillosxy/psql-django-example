from rest_framework import  serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    
    def get_email(self, obj):
        return obj.user.email
        
    class Meta:
        model = User
        fields = ('user', 'email', 'created_at', 'last_login')
