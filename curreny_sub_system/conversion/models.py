from django.db import models

# Create your models here.
class ConversionRate(models.Model):
    from_currency = models.CharField(max_length=4)
    to_currency = models.CharField(max_length=4)
    rate = models.IntegerField()

class ConversionHistory(models.Model):
    source_currency = models.CharField(max_length=4)
    target_currency = models.CharField(max_length=4)
    amount = models.IntegerField()
    conversion_rate = models.IntegerField()
