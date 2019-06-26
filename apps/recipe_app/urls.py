from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^welcome$',views.home),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^browse$', views.browse),
    url(r'^recipe/view/(?P<id>\d+)$',views.showrecipe),
    url(r'^search$',views.search),
    url(r'^surprise$',views.surprise)
]