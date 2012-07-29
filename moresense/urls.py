from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from moresense.spendings.views import add_spending, PersonDetailView, spendings_list, spendings_summary, spendings_export

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<identifier>[0-9a-f]+)/$', PersonDetailView.as_view()),
    url(r'^(?P<person_identifier>[0-9a-f]+)/spendings/add/$', add_spending, name="create"),
    url(r'^(?P<person_identifier>[0-9a-f]+)/spendings/$', spendings_list),
    url(r'^(?P<person_identifier>[0-9a-f]+)/spendings/summary$', spendings_summary),
    url(r'^(?P<person_identifier>[0-9a-f]+)/spendings/all$', spendings_export),

    url(r'^admin/', include(admin.site.urls)),
)
