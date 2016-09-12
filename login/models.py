from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#class TABLENAME(models.Model):
#   COLUMNNAME = models.COLUMNTYPE(default)

class UserProfile(models.Model):
    # Link to the authentication user module
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ssn = models.IntegerField()

    class Meta:
        abstract = True

class InternalUser(UserProfile):
    test = models.CharField(max_length=100)

class ExternalUser(UserProfile):
    test = models.CharField(max_length=100)
