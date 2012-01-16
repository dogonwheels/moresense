import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models.aggregates import Sum
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from moresense.spendings.models import  SpendingForm, Person, Spending

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


def spendings_list(request, person_identifier):
    person = get_object_or_404(Person, identifier=person_identifier)
    spendings = Spending.objects.filter(person__household=person.household).order_by("-when")[:10]
    return render_to_response("spendings/spending_list.html", {
        'person': person,
        'spendings': spendings
    }, context_instance=RequestContext(request))


def spendings_summary(request, person_identifier):
    person = get_object_or_404(Person, identifier=person_identifier)
    spendings = Spending.objects.filter(person__household=person.household)

    # TODO: Move these to household model manager - amount_this_week, amount_last_week...
    now = datetime.datetime.utcnow()
    start_of_day = datetime.datetime(day=now.day, month=now.month, year=now.year)

    # weekday is 0 on Monday
    start_of_week = start_of_day - datetime.timedelta(days=start_of_day.weekday())

    # If we were on the 1st, we're on day=1, the 0th day of the month
    start_of_month = start_of_day - datetime.timedelta(days=start_of_day.day - 1)
    start_of_last_week = start_of_week - datetime.timedelta(weeks=1)
    end_of_last_month = start_of_month - datetime.timedelta(days=1)
    start_of_last_month = end_of_last_month - datetime.timedelta(days=end_of_last_month.day - 1)

    # Pull out the total spent in some useful time periods
    totals = {
        'this_week': spendings.filter(when__gt=start_of_week).aggregate(Sum('amount'))['amount__sum'],
        'this_month': spendings.filter(when__gt=start_of_month).aggregate(Sum('amount'))['amount__sum'],
        'last_week': spendings.filter(when__lt=start_of_week, when__gt=start_of_last_week).aggregate(Sum('amount'))[
                     'amount__sum'],
        'last_month': spendings.filter(when__lt=start_of_month, when__gt=start_of_last_month).aggregate(Sum('amount'))[
                      'amount__sum']
    }

    return render_to_response("spendings/spending_summary.html", totals, context_instance=RequestContext(request))