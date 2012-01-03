from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from moresense.spendings.models import Spending, SpendingForm

class SpendingCreateView(CreateView):
    model = Spending

    def get_success_url(self):
        return reverse("create")

    def get_form_class(self):
        return SpendingForm

    def get_initial(self):
        # FIXME: set the person to be from construction - from the URL
        return {}
