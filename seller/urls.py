from django.urls import path
from .import views

urlpatterns=[
    path('home',views.seller_home, name='sellerhome')


]