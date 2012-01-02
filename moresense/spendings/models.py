from django.db import models

class Spending(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()
