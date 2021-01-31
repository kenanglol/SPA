from django.urls import path
from django.conf.urls import url

from .views import advert_create, advert_detail, advert_list

urlpatterns = [
    url(r'^advertdetail.html/$', advert_detail),
    url(r'^create/$', advert_create),
    url(r'^$', advert_list),
]