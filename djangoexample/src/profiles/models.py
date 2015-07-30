from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length = 1200)
    description = models.TextField(default='description default')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True) 
    location = models.CharField(max_length = 1200,default='My Location', blank=True)
    job = models.CharField(max_length = 1200,null=True)
    
    def __unicode__(self):
        return self.name

class userStripe(models.Model):
    stripe_id=models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

def my_callback(sender,request, user,  **kwargs):
        print("Request finished!")
        print(user)

user_logged_in.connect(my_callback)
