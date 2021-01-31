"""serviceapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from home.views import cat_view, home_view, home_view2
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^advert/', include('advert.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^$', home_view),
    url(r'^main2.html/$', home_view2),
    url(r'^main.html/$', home_view),
    url(r'^main2.html/categories.html/$', cat_view),
    url(r'^main2.html/categories.html/listAdverts.html/$',
        include('advert.urls')),
    url(r'^main2.html/categories.html/listAdverts.html/',
        include('advert.urls')),
    url(r'^main.html/categories.html/$', cat_view),
    url(r'^main.html/categories.html/listAdverts.html/$',
        include('advert.urls')),
    url(r'^main.html/categories.html/listAdverts.html/',
        include('advert.urls')),
    url(r'^categories.html/$', cat_view),
    url(r'^categories.html/listAdverts.html/$', include('advert.urls')),
    url(r'^categories.html/listAdverts.html/', include('advert.urls')),
]
