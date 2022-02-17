from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile',validators=[FileExtensionValidator(['png','jpg'])])

    def __str__(self):
        return self.user.username
    
    def last_login(self):
        return self.user.last_login