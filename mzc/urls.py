from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns=[
    path('',views.indexpage,name='index'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('home/',views.home,name='homepage')
]