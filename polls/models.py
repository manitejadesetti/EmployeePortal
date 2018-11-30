from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text= models.CharField(max_length=120)
    date= models.DateTimeField('date published')

    def was_published_recently(self):
        return self.date >=timezone.now()-datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text



