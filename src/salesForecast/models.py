from django.db import models

# Create your models here.
from django.db import models

from django.conf import settings

class Forcast(models.Model):
    
    start       = models.CharField(max_length=50)
    end         = models.CharField(max_length=50)
    user        =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    
class Sales(models.Model):
    
    product       = models.CharField(max_length=50)
    amount         = models.CharField(max_length=50)
    month         = models.CharField(max_length=50)
    user        =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 