from django.urls import path
from .import views
app_name='common'
urlpatterns=[
    path('index',views.common,name='index'),
   

]