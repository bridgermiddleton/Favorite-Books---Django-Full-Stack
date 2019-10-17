from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.booksmainpage),
    url(r'^addbook$', views.addbook),
    url(r'^books/(?P<bookid>\d+)$', views.bookdetails),
    url(r'^update/(?P<bookid>\d+)$', views.update),
    url(r'^deletebook/(?P<bookid>\d+)$', views.deletebook),
    url(r'^unfavorite/(?P<bookid>\d+)$', views.unfavorite),
    url(r'^favorite/(?P<bookid>\d+)$', views.favorite),
]