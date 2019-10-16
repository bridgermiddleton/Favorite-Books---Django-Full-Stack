from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wall$', views.wallpage),
    url(r'^post-message$', views.postmessage),
    url(r'^post-comment/(?P<messageid>\d+)$', views.postcomment),
    url(r'delete-comment/(?P<commentid>\d+)$', views.deletecomment),
    url(r'delete-message/(?P<messageid>\d+)$', views.deletemessage)
]