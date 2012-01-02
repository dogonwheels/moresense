from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from moresense.spendings.views import SpendingCreateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^spending/add/$', SpendingCreateView.as_view(), name="create"),

    url(r'^admin/', include(admin.site.urls)),
)
