from __future__ import unicode_literals

from django.db import models

# Create your models here.


class News_Data(models.Model):
    title = models.TextField()
    body = models.TextField()
