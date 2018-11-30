from __future__ import unicode_literals

from django.db import models
class AddEmployee(models.Model):
    username = models.CharField(max_length=120)
    emailId = models.EmailField(max_length=120,unique=True)
    mobileNumber = models.CharField(max_length=10)
    class Meta:
        unique_together=["emailId"]



