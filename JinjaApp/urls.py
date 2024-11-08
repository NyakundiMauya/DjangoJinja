from django.urls import path
from JinjaApp import  views



urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('contactus/',views.contactus,name='my_contactus'),
    path('services/',views.services,name='my_services'),


]