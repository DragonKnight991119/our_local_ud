from django.db import models

# Create your models here.
class SiteUrls(models.Model):
    sitename: models.CharField(max_length=40)