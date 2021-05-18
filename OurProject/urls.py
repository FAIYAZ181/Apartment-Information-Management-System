from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns=[
   path('base/',views.home),
   path('home/',views.insert_user_info,name='insert_user_info'),
   path('apartment/',views.insert_Apartment_info,name='insert_Apartment_info')

]