from django.db import models
from django.contrib.auth.models import User
from conversion.models import Conversion

class ConversionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversions = models.ForeignKey(Conversion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Conversion History"