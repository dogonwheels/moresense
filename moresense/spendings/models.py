import hashlib
import random
from django.db import models
from django.forms.models import ModelForm

def create_person_identifier():
    have_unique_identifier = False
    digest = ""
    while not have_unique_identifier:
        digest = hashlib.md5(str(random.random())).hexdigest()[:8]
        have_unique_identifier = Person.objects.filter(identifier=digest).count() == 0
    return digest


class Household(models.Model):
    name = models.CharField(max_length=50)


class Person(models.Model):
    household = models.ForeignKey(Household)
    name = models.CharField(max_length=50)
    identifier = models.CharField(max_length=50, default=create_person_identifier)


class Spending(models.Model):
    person = models.ForeignKey(Person)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()


class SpendingForm(ModelForm):
    class Meta:
        model = Spending
        fields = {"amount", "description"}
