from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^posts/(?P<id>\d+)/$',views.post_detail, name='post_detail'),
    url(r'^edit/(?P<id>\d+)/$', views.post_update, name='post_update'),
    url(r'^pappaya/$', views.pappaya, name='pappaya'),
    url(r'^lakshmi/$', views.lakshmi, name='lakshmi'),
    url(r'^sugar/$', views.sugarcane, name='sugarcane'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    ]
