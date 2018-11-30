from __future__ import unicode_literals

from django.db import models

class Test(models.Model):
    username = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    salary =models.IntegerField()


