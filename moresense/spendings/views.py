import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from moresense.spendings.models import  SpendingForm, Person

class PersonDetailView(DetailView):
    def get_object(self, queryset=None):
        identifier = self.kwargs["identifier"]
        try:
            person = Person.objects.get(identifier=identifier)
            return person
        except Person.DoesNotExist:
            raise Http404()


def add_spending(request, person_identifier):
    person = get_object_or_404(Person, identifier=person_identifier)
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        try:
            spending = form.save(commit=False)
            spending.person = person
            spending.when = datetime.datetime.utcnow()
            spending.save()
            messages.info(request, "%s added." % spending.amount)
            return HttpResponseRedirect(reverse("create", kwargs={"person_identifier": person_identifier}))
        except ValueError:
            pass
    else:
        form = SpendingForm()

    return render_to_response("spendings/spending_form.html", {
        'form': form,
        'person': person
    }, context_instance=RequestContext(request))

