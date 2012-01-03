from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from moresense.spendings.views import SpendingCreateView, PersonDetailView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^spending/add/$', SpendingCreateView.as_view(), name="create"),
    url(r'^(?P<identifier>[0-9a-f]+)/$', PersonDetailView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
