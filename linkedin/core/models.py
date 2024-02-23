from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.user.username
