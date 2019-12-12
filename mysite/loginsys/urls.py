from django.urls import path
from django.conf.urls import include , url
from . import views

urlpatterns = [
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^login/$',views.login, name='login'),
    ]
