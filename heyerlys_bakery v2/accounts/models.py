from django.db import models
from django.contrib.auth.models import User

class VerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Verification for {self.user.username}: {self.verified}"
