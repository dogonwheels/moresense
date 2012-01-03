from django.contrib import admin
from moresense.spendings.models import Person, Spending, Household

admin.site.register([Household, Person, Spending])
