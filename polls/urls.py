from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index1, name='index'),
    url(r'^sam$',views.sam),
    url(r'^getUsers/\d+$',views.getUsers),
]
