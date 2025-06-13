from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
# the user field in UserInfo (a OneToOneField) acts as a bridge to connect a UserInfo instance to a User instance, 
# linking the two models without user belonging to User.
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    profile_pic = models.ImageField(blank=True,upload_to='Content/media')

    def __str__(self):
        return self.user.username
    
