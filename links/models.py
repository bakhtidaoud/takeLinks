from django.db import models

# Create your models here.
class Links(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)