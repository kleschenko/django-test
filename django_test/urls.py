from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    url(r'^$', include('contacts.urls')),
    url(r'^logs/$', include('logs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
