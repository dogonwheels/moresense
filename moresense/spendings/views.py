from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from moresense.spendings.models import Spending, SpendingForm

class SpendingCreateView(CreateView):
    model = Spending

    def get_success_url(self):
        return reverse("create")

    def get_form_class(self):
        return SpendingForm
