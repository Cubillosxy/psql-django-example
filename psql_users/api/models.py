from django.db import models
from django.contrib.auth.models import User as UserD
from django.db.models.signals import post_save
from django.dispatch import receiver
from psql_users.settings import SIGN_API
import hashlib
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(UserD, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=40, null=True)
    last_login = models.CharField(max_length=40, null=True)

    #generate and return apiKey for this user
    def get_apiKey(self):
        sign = "%s-%s-%s" % (self.user.username, SIGN_API, self.user.email)
        return "trafilea" + hashlib.md5(sign.encode('utf-8')).hexdigest()

    def __unicode__(self):
        return unicode(self.user)
