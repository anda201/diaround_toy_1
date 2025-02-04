from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    image = models.ImageField(upload_to='user_img/', blank=True, null=True)
    user_comment = models.CharField(max_length=30)
    
    