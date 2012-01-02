from django.db import models
from django.forms.models import ModelForm

class Household(models.Model):
    name = models.CharField(max_length=50)

class Person(models.Model):
    household = models.ForeignKey(Household)
    name = models.CharField(max_length=50)
    identifier = models.CharField(max_length=50)

class Spending(models.Model):
    person = models.ForeignKey(Person)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()

class SpendingForm(ModelForm):
    class Meta:
        model = Spending
