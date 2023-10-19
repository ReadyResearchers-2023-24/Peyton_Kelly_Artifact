from django.urls import path
from . import views

urlpatterns = [
path('', views.ipaddress, name='ipaddress'),
path('', views.location, name='location'),
path('', views.public_ip, name='public_ip')

]