from django.conf.urls import url
from . import views

urlpatterns=[
<<<<<<< HEAD
    url(r'^login$',views.index),
    url(r'^$',views.test),
    url(r'^home$', views.home),
=======
    url(r'^$',views.home),
>>>>>>> ff2b0bab490ca380ca4c4bf0452052926c29001f
    url(r'^browse$', views.browse),
    url(r'^recipe/view/(?P<id>\d+)$',views.showrecipe),
    url(r'^search$',views.search)
]