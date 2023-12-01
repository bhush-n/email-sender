from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.


class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

# models.py


# class CustomUser(AbstractUser):
#     # Add any additional fields if needed
#     pass
