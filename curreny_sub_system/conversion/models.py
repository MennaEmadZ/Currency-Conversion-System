from django.db import models
from django.contrib.auth.models import User

class ConversionRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency} Rate"

class Conversion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    conversion_rate = models.ForeignKey(ConversionRate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_permanent = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Conversion"