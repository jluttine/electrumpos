from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'payments.views.home', name='home'),
    url(r'^m/(?P<uuid>.*?)$', 'payments.views.payment', name='payment'),

    url(r'^django_bitcoin/', include('django_bitcoin.urls')),

    # url(r'^electrumpos/', include('electrumpos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
