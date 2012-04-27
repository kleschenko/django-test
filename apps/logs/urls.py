from django.conf.urls import patterns, url
from django.views.generic import ListView
from logs.models import Entry

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        queryset=Entry.objects.order_by('-dtime')[:10],
            template_name='logs/index.html',
            context_object_name='logs',
        ), name='logs'),
)
