from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from moresense.spendings.models import Spending, SpendingForm, Person

class SpendingCreateView(CreateView):
    model = Spending

    def get_success_url(self):
        return reverse("create")

    def get_form_class(self):
        return SpendingForm

    def get_object(self, queryset=None):
        return Spending(person=Person.objects.get(identifier=self.kwargs['identifier']))


class PersonDetailView(DetailView):
    def get_object(self, queryset=None):
        identifier = self.kwargs["identifier"]
        try:
            person = Person.objects.get(identifier=identifier)
            return person
        except Person.DoesNotExist:
            raise Http404()
