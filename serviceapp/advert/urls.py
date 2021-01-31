from django.urls import path
from django.conf.urls import url

from .views import advert_create, advert_detail

urlpatterns = [
    url(r'^detail/$', advert_detail),
    url(r'^create/$', advert_create),
]