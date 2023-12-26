from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
#from channels.layers import get_channel_layer
import re
from django.core.validators import RegexValidator
#import json

# Create your models here.
# Subscriber
class Subscriber(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	mobile = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
	userid = models.CharField(max_length=50)
	img = models.ImageField(null=True)
	

		
# @receiver(post_save,sender=User)
# def create_subscriber(sender,instance,created,**kwrags):
# 	if created:
# 		Subscriber.objects.create(user=instance)
		
# trainer
class Trainer(models.Model):
	full_name=models.CharField(max_length=100)
	details = models.CharField(max_length= 100)




