from django.db import models
from django.contrib.auth.models import User as UserD
from psql_users.settings import SIGN_API
import hashlib
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(UserD, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=40, blank=True)
    last_login = models.CharField(max_length=40, blank=True)

    #generate and return apiKey for this user
    def get_apiKey(self):
        sign = "%s-%s-%s-%s" % (self.user.username, SIGN_API, self.user.email, self.user.password)
        return hashlib.md5(sign).hexdigest()

    def __unicode__(self):
        return unicode(self.user)
