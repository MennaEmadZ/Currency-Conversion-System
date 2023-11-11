from django.db import models
from django.contrib.auth.models import User

class ConversionRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency} Rate"

class CurrencyConversion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=12, decimal_places=6)
    conversion_rate = models.DecimalField(max_digits=12, decimal_places=6, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='temporary', max_length=10)
    
    def __str__(self):
        return f"{self.from_currency} to {self.to_currency} with customer {self.user.username}"

    def update_status(self):
        # Check if 48 hours have passed since creation
        if (datetime.datetime.now() - self.created_at.replace(tzinfo=None)) > datetime.timedelta(hours=48):
            self.status = 'permanent'
            self.save()



