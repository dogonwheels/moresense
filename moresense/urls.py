from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from moresense.spendings.views import add_spending, PersonDetailView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<identifier>[0-9a-f]+)/$', PersonDetailView.as_view()),
    url(r'^(?P<person_identifier>[0-9a-f]+)/spending/add/$', add_spending, name="create"),

    url(r'^admin/', include(admin.site.urls)),
)
