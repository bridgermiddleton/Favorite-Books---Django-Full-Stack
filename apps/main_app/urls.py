from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout', views.logout),
]