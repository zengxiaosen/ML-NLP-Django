from django.conf.urls import url,include

from . import views
urlpatterns = [

    url(r'^index/', views.index),
    url(r'^provice/', views.provice, name='provice'),
    url(r'^city/', views.city, name='city'),
    url(r'^hello/', views.city, name='hello'),
]
