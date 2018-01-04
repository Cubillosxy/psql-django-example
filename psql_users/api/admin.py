from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'last_login', 'apiKey')

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def apiKey(self, obj):
        return obj.get_apiKey()
    
admin.site.register(User, UserAdmin)