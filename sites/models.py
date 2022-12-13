from django.db import models


# Create your models here.
class Sites(models.Model):
  
    domain_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    
