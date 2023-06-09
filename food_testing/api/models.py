from django.db import models

from rest_framework_api_key.models import APIKey
APIKey.objects.count()
api_key, key = APIKey.objects.create_key(name="my-remote-service")
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.
class FoodData (models.Model):
    #ph_value = models.DecimalField()
    name = models.CharField(max_length=256,null=True)
    humidity = models.DecimalField(max_digits=5,null=True, decimal_places=2)
    methane = models.DecimalField(max_digits=5,null=True, decimal_places=2)
    temperature = models.DecimalField(max_digits=5,null=True, decimal_places=2)
    Quality = models.CharField(max_length=256,null=True)
    #actions = ['export_data']

class FoodItem(models.Model):
    item = models.CharField(max_length=15)
    data = models.ForeignKey(FoodData,on_delete=models.CASCADE, null=True)
    


    
