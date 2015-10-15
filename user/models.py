from django.db import models

# Create your models here.
class Gis(models.Model):
	item = models.CharField(max_length=50)
	lat = models.CharField(max_length=12)
	lon = models.CharField(max_length=12)