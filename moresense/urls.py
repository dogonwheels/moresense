from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from django.views.generic.edit import CreateView
from moresense.spendings.models import Spending

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^spending/add/$', CreateView.as_view(model=Spending, success_url=".")),

    url(r'^admin/', include(admin.site.urls)),
)
