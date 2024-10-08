from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import secrets
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    

    def __str__(self):
        return self.email

class Otp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
    otp_created_at = models.DateTimeField(auto_now_add=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)



    def __str__(self):
        return self.user.username
    

class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="images")
    season = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.user.username
